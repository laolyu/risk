# coding:utf-8
import pytest


class TestOne:
    @pytest.mark.dependency()
    def test_a(self):
        assert False

    @pytest.mark.dependency(depends=["TestOne::test_a"])
    def test_b(self):
        assert True

    @pytest.mark.dependency(depends=["TestOne::test_a"])
    def test_c(self):
        assert True

    @pytest.mark.dependency(depends=["TestOne::test_b", "TestOne::test_c"])
    def test_d(self):
        assert True


if __name__ == '__main__':
    pytest.main()
