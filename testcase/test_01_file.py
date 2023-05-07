# coding:utf-8
import pytest
from pages.app import App


class TestFile:
    def setup(self):
        self.file_page = App.dr().to_file()

    @pytest.mark.dependency()
    @pytest.mark.dependency(depends=["testcase/test_00_apk.py::TestApk::test_apk_po"], scope="session")
    def test_file_po(self):
        assert '风险提示' in self.file_page.get_alter_text()
