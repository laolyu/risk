# coding:utf-8
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MessagecontentPage(BasePage):
    # 页面元素定位
    _messagecontent = (By.ID, 'com.huawei.systemmanager:id/messagecontent')

    # 页面元素对象
    def get_messagecontent(self):
        return self.find_click(self._messagecontent)
