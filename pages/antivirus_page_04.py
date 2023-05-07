# coding:utf-8
from time import sleep

from loguru import logger

from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class AntivirusPage(BasePage):
    # 页面元素定位
    # _uninstall_at_once = (By.XPATH, "//*[contains(@text,'风险详情')]")

    # 页面元素对象
    def get_uninstall_text(self):
        return self.alter_risk().text
