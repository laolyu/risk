# coding:utf-8
from time import sleep

from loguru import logger
import pytest
from pages.app import App


class TestKnown:
    def setup(self):
        self.known_page = App.dr().to_known()

    @pytest.mark.dependency()
    @pytest.mark.dependency(depends=["testcase/test_01_file.py::TestFile::test_file_po"], scope="session")
    def test_known_po(self):
        assert self.known_page.get_known_risk().is_displayed()
