import subprocess
from loguru import logger
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from pages.base_page import BasePage
from pages.file_page import FilePage


# from pages.file_page import FilePage


class MainPage(BasePage):
    # _search_locator = (By.ID, "com.xueqiu.android:id/home_search")
    _file_locator = (By.ID, 'android:id/title_template')

    # def to_search(self):
    #     # todo: too slow
    #     self.find_element_and_click(self._search_locator)
    #     return SearchPage(self.driver)

    def to_file(self):
        udid = '192.168.0.197:5555'
        apkpath = r'C:\abtest\automation\UI\risk\apk\hyd_v1.4.3-dyn-2023-0223-18-04-debug-king-mjbv3.2.97-nothidden-all.apk'
        cmd = f'adb -s {udid} install {apkpath}'
        cmd_password = f'adb -s  {udid} shell input text 123456'
        try:
            p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            out, err = p.communicate(timeout=10)
            out_info = out.decode('gbk')
            logger.info(out_info)
        except Exception as e:
            logger.info(e)
        logger.info('-1111111111111')
        return FilePage(self.driver)
