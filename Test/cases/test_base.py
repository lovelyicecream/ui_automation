# -*- coding:utf-8 -*-

import pytest

from Test.utils.base import Browser
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("browser")
class TestFix(object):
    """
        测试utils.base文件中的方法
    """

    def test_baidu(self, browser):
        driver = Browser(browser)
        driver.open_url("https://www.baidu.com/")
        text = driver.get_element_text("hao123", By.PARTIAL_LINK_TEXT)
        assert "000" in text

    def test_send_keys(self, browser):
        driver = Browser(browser)
        driver.open_url("https://www.baidu.com/")
        driver.send_keys("python", "kw", By.ID)
        driver.click_element("su", By.ID)
        assert "python" in driver.get_title()

    def test_element_dispaly(self, browser):
        driver = Browser(browser)
        driver.open_url("https://www.baidu.com/")
        res = driver.is_element_display("su", By.ID)
        assert res is True

    def test_get_attribute(self, browser):
        driver = Browser(browser)
        driver.open_url("https://www.baidu.com/")
        attr = driver.get_element_attribute("su", By.ID)
        assert "Python" in attr

    def test_url_change(self, browser):
        driver = Browser(browser)
        driver.open_url("https://www.baidu.com/")
        last_url = driver.get_current_url()
        driver.click_element("hao", By.PARTIAL_LINK_TEXT)
        res = driver.is_url_changed(last_url)
        assert res is True

    def test_cookies(self, browser):
        driver = Browser(browser)
        driver.open_url("https://www.baidu.com/")
        cookies = driver.get_cookies()
        print("Get Cookies: ", cookies)

    def test_scroll_to(self, browser):
        driver = Browser(browser)
        driver.open_url("https://www.baidu.com/")
        driver.send_keys("python", "kw", By.ID)
        driver.click_element("su", By.ID)
        driver.scroll_to(0, 2000)

    def test_get_element_size(self, browser):
        driver = Browser(browser)
        driver.open_url("https://www.baidu.com/")
        (height, width) = driver.get_element_size("su", By.ID)
        assert (36, 100) == (height, width)

    def test_javascript_click(self, browser):
        driver = Browser(browser)
        driver.open_url("https://www.baidu.com/")
        driver.send_keys("python", "kw", By.ID)
        driver.javascript_click("su", By.ID)

if __name__ == '__main__':
    pytest.main(["-s", "test_fix.py"])
