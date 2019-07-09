# -*- coding:utf-8 -*-
import time
from selenium.common.exceptions import TimeoutException, NoSuchElementException, UnexpectedAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Test.utils.logger import Log

logger = Log()


class Browser(object):
    """
        二次封装浏览器常用操作
    """

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def get_page_source(self):
        return self.driver.page_source

    def refresh_page(self):
        self.driver.refresh()

    def get_current_url(self):
        return self.driver.current_url

    def get_title(self):
        return self.driver.title

    def close_window(self):
        self.driver.close()

    def find_element(self, locator, by=By):
        try:
            element = self.driver.find_element(by=by, value=locator)
        except NoSuchElementException as e:
            logger.error("NoSuchElementException: ", e)

        return element

    def find_elements(self, locator, by=By):
        try:
            elements = self.driver.find_elements(by=by, value=locator)
        except NoSuchElementException as e:
            logger.error("NoSuchElementException: ", e)

        return elements

    def is_element_display(self, locator, by=By, wait_time=5):
        try:
            result = WebDriverWait(self.driver, wait_time).until(
                lambda driver: driver.find_element(by=by, value=locator).is_displayed())
        except TimeoutException as e:
            logger.error("TimeoutException: ", e)
            result = False
        return result

    def get_element(self, locator, by=By):
        if self.is_element_display(locator=locator, by=by):
            return self.find_element(locator, by)

    def click_element(self, locator, by=By, wait_time=2):
        element = WebDriverWait(self.driver, wait_time).until(EC.element_to_be_clickable((by, locator)))
        element.click()

    def send_keys(self, text, locator, by=By):
        element = self.find_element(by=by, locator=locator)
        element.clear()
        element.send_keys(text)

    def get_element_text(self, locator, by=By):
        if self.is_element_display(by=by, locator=locator):
            return self.find_element(by=by, locator=locator).text

    def get_element_attribute(self, locator, by=By, attr="value"):
        if self.is_element_display(by=by, locator=locator):
            return self.find_element(by=by, locator=locator).get_attribute(attr)

    def is_url_changed(self, last_url, timeout=2.0):
        url = self.get_current_url()
        while timeout > 0:
            if url != last_url:
                return True
            time.sleep(0.5)
            timeout -= 0.5
            url = self.current_url()
        return False

    def is_alert_present(self, wait_time=3):
        try:
            WebDriverWait(self.driver, wait_time).until(EC.alert_is_present())
            return True
        except UnexpectedAlertPresentException as e:
            logger.error("UnexpectedAlertPresentException: ", e)
            return False

    def accept_alert(self):
        if self.is_alert_present():
            alert = self.driver.switch_to.alert
            alert.accept()
            return alert.text

    def get_cookies(self):
        return self.driver.get_cookies()

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    def switch_frame(self, locator, by=By):
        iframe = self.find_element(locator, by)
        self.driver.switch_to_frame(iframe)

    def get_current_window_handle(self):
        self.driver.current_window_handle

    def get_window_handles(self):
        self.driver.window_handles

    def get_window_handle(self, index):
        self.driver.window_handles[index]

    def execute_js(self, script, *args):
        return self.driver.execute_script(script, *args)

    def javascript_click(self, locator, by=By):
        self.execute_js('arguments[0].click();', self.get_element(locator, by))

    def scroll_to(self, width, height):
        script = "window.scrollTo(%d, %d);" % (int(width), int(height))
        self.execute_js(script)

    def get_element_size(self, locator, by=By):
        element = self.find_element(locator, by)
        height = self.driver.execute_script(
            "return arguments[0].offsetHeight", element
        )
        width = self.driver.execute_script(
            "return arguments[0].offsetWidth", element
        )
        return height, width
