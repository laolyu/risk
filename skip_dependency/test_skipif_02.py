# coding:utf-8
import pytest


@pytest.mark.skipif('test_a')
def test_b():
    assert True

# @pytest.mark.skipif(pytest.raises(AssertionError, lambda: None), reason="test_a failed")
# def test_b():
#     assert True
