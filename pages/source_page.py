# coding:utf-8
from pages.base_page import BasePage


class SourcePage(BasePage):
    # 页面元素定位
    _risk_icon = 'com.huawei.appmarket:id/tips_card_risk_icon'
    _continue_hw = 'com.huawei.appmarket:id/hidden_card_install_button_continue'

    # 页面元素对象
    def risk_source(self):
        self.find_element(self._risk_icon)
        return self

    def risk_source_c(self):
        self.find_element_and_click(self._continue_hw)
        return self
