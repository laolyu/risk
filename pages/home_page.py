# coding:utf-8
import subprocess
import time
import pyperclip
from loguru import logger
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BaseFunc


class Page_one(BaseFunc):
    # 页面元素定位
    alertTitle = ('AppiumBy.ID', 'android:id/alertTitle')
    alert_continue = ('AppiumBy.ID', 'android:id/button1')

    continue_button = ('AppiumBy.ID', 'com.android.packageinstaller:id/continue_button')
    ok_button = ('AppiumBy.ID', 'com.android.packageinstaller:id/ok_button')
    done_button = ('AppiumBy.ID', 'com.android.packageinstaller:id/done_button')

    risk_icon = ('AppiumBy.ID', 'com.huawei.appmarket:id/tips_card_risk_icon')
    continue_hw = ('AppiumBy.ID', 'com.huawei.appmarket:id/hidden_card_install_button_continue')

    # 页面元素对象
    def get_alertTitle_obj(self):
        ele = self.locator_ele(Page_one.alertTitle)
        return ele

    def get_alert_continue_obj(self):
        ele = self.locator_ele(Page_one.alert_continue)
        return ele

    def get_continue_button_obj(self):
        ele = self.locator_ele(Page_one.continue_button)
        return ele

    def get_ok_button_obj(self):
        ele = self.locator_ele(20, Page_one.ok_button)
        return ele

    def get_done_button_obj(self):
        ele = self.locator_ele(20, Page_one.done_button)
        return ele

    def get_risk_icon_obj(self):
        ele = self.locator_ele(30, Page_one.risk_icon)
        return ele

    def get_continue_hw_obj(self):
        ele = self.locator_ele(Page_one.continue_hw)
        return ele

    # 页面对象操作
    def begin_alter(self):
        self.get_alertTitle_obj()
        BaseFunc().take_screenshot()

    def begin_alter_c(self):
        obj = self.get_alert_continue_obj()
        BaseFunc().take_screenshot()
        obj.click()
        BaseFunc().take_screenshot()

    def risk_source(self):
        self.get_risk_icon_obj()
        BaseFunc().take_screenshot()

    def risk_source_c(self):
        obj = self.get_continue_hw_obj()
        BaseFunc().take_screenshot()
        obj.click()
        BaseFunc().take_screenshot()

    def continue_btn(self):
        obj = self.get_continue_button_obj()
        BaseFunc().take_screenshot()
        obj.click()
        BaseFunc().take_screenshot()

    def ok_btn(self):
        obj = self.get_ok_button_obj()
        BaseFunc().take_screenshot()
        obj.click()
        BaseFunc().take_screenshot()

    def done_btn(self):
        obj = self.get_done_button_obj()
        BaseFunc().take_screenshot()
        obj.click()
        BaseFunc().take_screenshot()

    def alert_installed(self):
        obj = self.get_done_button_obj()
        BaseFunc().take_screenshot()
        obj.click()
        BaseFunc().take_screenshot()


def apkpath():
    # title = 'paste'
    # message = 'Please enter the apk path.                             '
    # path_input = dialogg.get_text_input(title, message)

    # path_input = crt.Dialog.Prompt(
    #     "Please enter the apk path.Thank you!",
    #     "paste",
    #     "",
    #     False)

    path_input = pyperclip.paste()
    logger.info(path_input)
    path_base = r'F:/apps/apk/new/'
    file = path_base + path_input + '.apk'
    return file

# try:
#     file = apkpath()
#     f = open(file)
#     f.close()
#     driver = driver()
#     AppInst(driver, file)
#     driver.quit()
# except IOError as e:
#     logger.info(e)
# except Exception as e:
#     logger.info(e)
