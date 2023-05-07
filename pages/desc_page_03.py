# coding:utf-8
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class DescPage(BasePage):
    # 页面元素定位
    _risk_desc = (By.ID, 'com.huawei.appmarket:id/app_risk_desc_title')

    # 页面元素对象
    def get_risk_desc(self):
        return self.find_ele(self._risk_desc)
