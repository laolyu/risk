# coding:utf-8
# test_01.py
def test_a():
    assert True


# test_02.py
import pytest


# @pytest.mark.skipif('test_a()')
# def test_b():
#     assert True

@pytest.mark.skipif(pytest.raises(AssertionError, lambda: None), reason="test_a failed")
def test_b():
    assert True


if __name__ == '__main__':
    pytest.main()
