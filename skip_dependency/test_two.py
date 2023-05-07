# coding:utf-8
from time import sleep

import pytest


class TestTwo:
    @pytest.mark.dependency()
    @pytest.mark.dependency(depends=["skip_dependency/test_one.py::TestOne::test_a"], scope='session')
    def test_b(self):
        sleep(1)
        assert 2 == 2
