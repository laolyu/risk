# coding:utf-8
from pages.base_page import BasePage


class InstalledPage(BasePage):
    # 页面元素定位
    _alert_installed = 'com.huawei.systemmanager:id/messagecontent'

    # 页面元素对象
    def alert_installed(self):
        self.find_element_and_click(self._alert_installed)
        return self
