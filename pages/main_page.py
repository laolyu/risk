import subprocess
import time
from loguru import logger
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.file_page_01 import FilePage
from pages.known_page_02 import KnownPage
from pages.desc_page_03 import DescPage
from pages.antivirus_page_04 import AntivirusPage
from pages.messagecontent_page_05 import MessagecontentPage


class MainPage(BasePage):
    _cmd_password = 'adb shell input text 2212'
    _install_succ = (By.ID, 'com.huawei.appmarket:id/install_confirm_normal_loading_text')
    _alert_continue = (By.ID, 'android:id/button1')
    _to_learn_risk = (By.ID, 'com.huawei.appmarket:id/hidden_card_install_button_continue')
    _checkbox = (By.ID, 'com.huawei.appmarket:id/hidden_card_checkbox')
    _install_continue = (By.ID, 'com.huawei.appmarket:id/hidden_card_install_button_continue')
    _messagecontent = (By.ID, 'com.huawei.systemmanager:id/messagecontent')

    def to_file(self):
        # udid = '192.168.0.197:5555'
        # apkpath = r'C:\abtest\automation\UI\risk\apk\hyd_v1.4.3-dyn-2023-0223-18-04-debug-king-mjbv3.2.97-nothidden-all.apk'
        # cmd = f'adb install {apkpath}'
        # try:
        #     p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #     out, err = p.communicate(timeout=10)
        #     out_info = out.decode('gbk')
        #     logger.info(out_info)
        #     # return AntivirusPage(self.driver)
        # except Exception as e:
        #     logger.info(e)
        return FilePage(self.driver)

    def to_known(self):
        self.alter_risk().accept()
        # self.find_click(self._alert_continue)
        return KnownPage(self.driver)

    def to_desc(self):
        self.find_click(self._to_learn_risk)
        return DescPage(self.driver)

    def to_antivirus(self):
        self.find_click(self._checkbox)
        self.find_click(self._install_continue)
        time.sleep(2)
        subprocess.Popen(self._cmd_password, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return AntivirusPage(self.driver)

    def to_messagecontent(self):
        self.find_click(self._messagecontent)
        return MessagecontentPage(self.driver)
