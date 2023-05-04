# coding:utf-8
from pages.base_page import BasePage


class BtnPage(BasePage):
    # 页面元素定位
    _continue_button = (By.ID, 'com.android.packageinstaller:id/continue_button')
    _ok_button = (By.ID, 'com.android.packageinstaller:id/ok_button')
    _done_button = (By.ID, 'com.android.packageinstaller:id/done_button')

    # 页面元素对象
    def btn_continue(self):
        self.find_element_and_click(self._continue_button)
        return self

    def btn_ok(self):
        self.find_element_and_click(self._ok_button)
        return self

    def btn_done(self):
        self.find_element_and_click(self._done_button)
        return self
