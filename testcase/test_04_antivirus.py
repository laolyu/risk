# coding:utf-8
import time

from loguru import logger
import pytest
from pages.app import App


class TestAntivirus:
    def setup(self):
        self.antivirus_page = App.dr().to_antivirus()

    @pytest.mark.dependency()
    @pytest.mark.dependency(depends=["testcase/test_03_desc.py::TestDesc::test_desc_po"], scope="session")
    def test_antivirus_po(self):
        time.sleep(5)
        assert '风险详情' in self.antivirus_page.get_uninstall_text()
