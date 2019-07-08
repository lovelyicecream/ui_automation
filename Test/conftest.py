# -*- coding:utf-8 -*-

"""
yield 和addfinalizer 方法都是在测试完成后呼叫相应的代码。
不同的是：
1. addfinalizer 可以注册多个终结函数
2. 返些终结方法总是会被执行，无论在之前的 setup code 有没有抛出错误。
addfinalizer 对于正确关闭所有的 fixture 创建的资源非常便利，即使在创建戒获取时失败

"""
import pytest


# @pytest.fixture(scope="module")
# def login():
#     print("\n我是module登录")
#     yield
#     print("我是module退出")

@pytest.fixture(scope="module")
def login(request):
    print("\n我是登录")

    def fin_b():
        print("我是第二次退出")
    request.addfinalizer(fin_b)

    def fin_a():
        print("我是第一次退出")
    request.addfinalizer(fin_a)


@pytest.fixture(scope="module", autouse=False)
def open(request):
    print("打开浏览器")

    def fin():
        print("关闭浏览器")
    request.addfinalizer(fin)
