# -*- coding:utf-8 -*-

import pytest


@pytest.mark.parametrize("number, expected", [
    ("3+5", 8),
    ("2+4", 6),
    pytest.param("6 * 9", 42, marks=pytest.mark.xfail)  # 标记为失败的用例就不运行了，直接跳过显示xfailed
])
def test_eval(number, expected):
    assert eval(number) == expected


if __name__ == "__main__":
    pytest.main(["-s", "test_param.py"])

