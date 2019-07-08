# -*- coding:utf-8 -*-

import pytest


class TestClass(object):

    @pytest.mark.daily  # 使用mark.daily标记为白天运行的用例
    def test_send_http(self):
        a, b = 1, 2
        c = a + b
        assert c == 3

    @pytest.mark.daily
    @pytest.mark.nightly  # 使用mark.nightly标记为晚上运行的用例
    def test_something_quick(self):
        assert 'se' in 'selenium'

    def test_another(self):
        pass


if __name__ == "__main__":
    pytest.main(["-s", "test_mark.py", "-m=webtest"])
