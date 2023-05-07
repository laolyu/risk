# coding:utf-8
from loguru import logger
import pytest
from pages.app import App


class TestDesc:
    def setup(self):
        self.desc_page = App.dr().to_desc()

    @pytest.mark.dependency()
    @pytest.mark.dependency(depends=["testcase/test_02_known.py::TestKnown::test_known_po"], scope="session")
    def test_desc_po(self):
        assert self.desc_page.get_risk_desc().is_displayed()
