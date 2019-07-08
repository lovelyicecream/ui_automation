# -*- coding:utf-8 -*-

import pytest


class TestFix(object):
    def test_a(self):
        assert "f" in "fuck"

if __name__ == '__main__':
    pytest.main(["-s", "test_fix.py"])
