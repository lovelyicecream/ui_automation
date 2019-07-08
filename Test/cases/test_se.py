# -*- coding:utf-8 -*-

import pytest
from Test.common import config


@pytest.mark.usefixtures("browser")
class TestSe(object):
    @pytest.mark.parametrize("url, text", [
        (config.url, u"百度"),
        ("https://cn.bing.com/", "Bingo"),
    ])
    def test_url(self, browser, url, text):
        """
        hello world
        """
        browser.get(url)
        assert text in browser.title


if __name__ == '__main__':
    pytest.main(["-s", "test_se.py", "--cmdopt=headless", "--html=../reports/report.html"])


# 命令行指定浏览器: --cmdopt=firefox
# 命令行指定测试报告: --html=../report/report.html
# 命令行合并css样式到html报告: --self-contained-html
# 命令行使用pytest-rerunfailures: --reruns 1
