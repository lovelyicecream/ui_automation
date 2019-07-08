# -*- coding:utf-8 -*-
import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default="chrome", help="my option: chrome or firefox"
    )


@pytest.fixture(scope='function', autouse=False)
def browser(request):
    cmdopt = request.config.getoption("--cmdopt")
    global driver
    if cmdopt == "chrome":
        driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
    elif cmdopt == "firefox":
        driver = webdriver.Firefox()

    # driver.maximize_window()

    def fin():
        driver.quit()

    request.addfinalizer(fin)
    return driver


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            screen_img = _capture_screenshot()
            if file_name:
                html = '<div><img src="data:image/png;base64,%s" alt="screenshot" style="width:600px;height:300px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % screen_img
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot():
    return driver.get_screenshot_as_base64()


# 自定义html报告的Environment
# def pytest_configure(config):
#     config._metadata['Driver'] = "Chrome"

from datetime import datetime
from py.xml import html


# 优化Results表格中增加用例描述
@pytest.mark.optionalhook
def pytest_html_results_table_header(cells):
    cells.insert(2, html.th('Description'))
    cells.insert(1, html.th('Time', class_='sortable time', col='time'))
    cells.pop()


@pytest.mark.optionalhook
def pytest_html_results_table_row(report, cells):
    cells.insert(2, html.td(report.description))
    cells.insert(1, html.td(datetime.utcnow(), class_='col-time'))
    cells.pop()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    report.description = str(item.function.__doc__)
