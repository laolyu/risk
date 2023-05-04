# coding:utf-8
from loguru import logger
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FilePage(BasePage):
    logger.info('22222222222')
    # 页面元素定位
    _alertTitle = (By.ID, 'android:id/alertTitle')
    _alert_continue = (By.ID, 'android:id/button1')
    _file_alter = (By.ID, 'android:id/title_template')

    # 页面元素对象

    def file_alertTitle(self):
        self.find_element_and_click(self._alertTitle)
        return self

    def fie_alert_continue(self):
        self.find_element_and_click(self._alert_continue)
        return self

    def get_alter(self):
        return self.find_element(self._file_alter)
