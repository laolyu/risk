# coding:utf-8
from appium import webdriver
from loguru import logger
from selenium.webdriver.remote.webdriver import WebDriver
from pages.main_page import MainPage


class App:
    driver: webdriver = None

    def __init__(self, driver):
        logger.info('000033333300')
        self.driver = driver

    @classmethod
    def dr(cls):
        """
       @classmethod装饰器来定义一个类方法，用来返回一个App类的实例，这样就不需要在每个测试类中创建一个App对象
       """
        caps = {'platformName': 'android',
                'deviceName': 'hw',
                'newCommandTimeout': 20,
                'automationName': 'UiAutomator2',
                # 'appPackage': 'com.xueqiu.android',
                # 'appActivity': '.view.WelcomeActivityAlias',
                # 'autoGrantPermissions': 'true',  #自动同意权限申请
                # 'udid': 'emulator-5556',
                # 'chromedriverExecutable': '/Users/seveniruby/projects/chromedriver/2.20/chromedriver',
                'showChromedriverLog': True}

        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
        cls.driver.implicitly_wait(10)
        logger.info('driver is ready')
        # yield cls.driver
        # cls.driver.quit()
        return MainPage(cls.driver)
