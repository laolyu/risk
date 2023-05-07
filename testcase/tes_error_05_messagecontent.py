# coding:utf-8
from loguru import logger
import pytest
# from pages.file_page import FilePage
from pages.app import App


class TestMessagecontent:
    def setup(self):
        self.messagecontent_page = App.dr().to_messagecontent()

    # @pytest.mark.dependency(depends=["testcase/test_04_antivirus::TestAntivirus::test_desc_po"], scope="session")
    def test_messagecontent_po(self):
        assert self.messagecontent_page.get_messagecontent().is_displayed()
        # self.messagecontent_page.fie_alert_continue()
