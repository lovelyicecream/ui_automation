# -*- coding:utf-8 -*-
"""
调用 fixture 三种方法
1.函数戒类里面方法直接传 fixture 的函数参数名称
2.使用装饰器@pytest.mark.usefixtures()修饰
3.autouse=True 自动使用

"""
import pytest


@pytest.mark.usefixtures("login")
class TestHello(object):
    def test_s4(self):
        print("用例4：登录之后其它动作111")

    def test_s5(self):
        print("用例5：不需要登录，操作222")


if __name__ == "__main__":
    pytest.main(["-s",  "test_hello.py"])
