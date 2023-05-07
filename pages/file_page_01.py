# coding:utf-8
from loguru import logger
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class FilePage(BasePage):
    # 页面元素定位
    # _alter = (By.ID, 'android:id/alertTitle')

    # 页面元素对象
    def get_alter_text(self):
        return self.alter_risk().text
