# coding:utf-8
from time import sleep

import pytest


@pytest.mark.dependency()
def test_aa():
    sleep(1)
    assert 2 == 2

class TestOne:

    @pytest.mark.dependency()
    def test_a(self):
        sleep(1)
        assert 1 == 1

    # @pytest.mark.dependency(depends=["test_aa"], scope='class')
    # def test_b(self):
    #     sleep(2)
    #     assert 2 == 2


# if __name__ == '__main__':
#     pytest.main()
