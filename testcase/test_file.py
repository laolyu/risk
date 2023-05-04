# coding:utf-8
from loguru import logger
import pytest
# from pages.file_page import FilePage
from pages.app import App


class TestFile:

    def setup(self):
        logger.info('111111111')
        self.file_page = App.dr().to_file()

    def test_to_file(self):
        logger.info('22222222220')
        assert 1 == 1
        # file_page = FilePage(App.driver)
        # main_page.to_file()  # 使用app对象来访问main_page属性
        # assert file_page.get_alter().is_displayed()

    # def test_get_alter(self, cap):
    #     app = cap
    #     file_page = FilePage(app.driver)
    #     assert file_page.get_alter().text == "风险提示"
