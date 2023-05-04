# coding:utf-8
import datetime
import inspect
from loguru import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
    _black_list = [
        (By.ID, 'image_cancel'),
        (By.ID, 'tips')
    ]

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, locator):
        try:
            # self.take_screenshot()
            logger.info(f'finding {locator}')
            return self.driver.find_element(*locator)
        except:
            self.handle_exception()
            return self.driver.find_element(*locator)

    def find_element_and_click(self, locator):
        try:
            logger.info(f'found locator and click it')
            # self.take_screenshot()
            # 如果click也有异常，可以这样处理
            self.find_element(locator).click()
        except:
            self.handle_exception()
            self.find_element(locator).click()

    def handle_exception(self):
        logger.info('sth may exception')
        self.driver.implicitly_wait(0)
        for locator in self._black_list:
            elements = self.driver.find_elements(*locator)
            self.take_screenshot()

            if len(elements) >= 1:
                # todo: 不是所有的弹框处理都是要点击弹框，可根据业务需要自行封装
                logger.info(f'found locator and click it')
                elements[0].click()
            else:
                logger.info(f'{locator} not found')

            # todo: 私用page source会更快的定位

            # page_source=self.driver.page_source
            # if 'image_cancel' in page_source:
            #     self.driver.find_element(*locator).click()
            # elif 'tips' in page_source:
            #     pass

        self.driver.implicitly_wait(10)

    def take_screenshot(self):
        # 获取当前时间
        now = datetime.datetime.now()
        # 格式化时间戳
        timestamp = now.strftime('%Y-%m-%d %H:%M:%S')
        # 获取设备名称
        device_name = self.driver.desired_capabilities['deviceName']
        # 获取函数名称
        function_name = inspect.currentframe().f_back.f_code.co_name
        # 拼接文件名
        filename = f'{device_name}_{timestamp}_{function_name}.png'
        # 截图
        self.driver.save_screenshot(filename)
