# coding:utf-8
from time import sleep

import pytest


class TestThree:

    @pytest.mark.dependency(depends=["skip_dependency/test_one.py::TestOne::test_a", 'skip_dependency/test_two.py::TestTwo::test_b'],scope='session')
    def test_c(self):
        sleep(2)
        assert 3 == 4
