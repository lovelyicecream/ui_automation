# -*- coding:utf-8 -*-

import pytest
import sys


@pytest.mark.skip(reason="no way of currently testing")  # 使用skip直接跳过
def test_the_unknown():
    assert "aaa" == "bbb"


@pytest.mark.skipif(sys.version_info > (2, 7), reason="requires python3 or higher")  # 使用skipif在条件成立下跳过
def test_condition():
    assert sys.version_info == (2, 7)


if __name__ == "__main__":
    pytest.main(["-s", "test_skip.py"])
