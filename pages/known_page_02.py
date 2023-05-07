# coding:utf-8
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class KnownPage(BasePage):
    # 页面元素定位
    _risk_icon = (By.ID, 'com.huawei.appmarket:id/tips_card_title')

    # 页面元素对象
    def get_known_risk(self):
        return self.find_ele(self._risk_icon)
