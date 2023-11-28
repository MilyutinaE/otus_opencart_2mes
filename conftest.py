import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
import os.path
import logging
import datetime


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="Browser. Default option is chrome")
    parser.addoption("--drivers_folder", default="D:\\drivers\\", help="Path to the drivers")
    parser.addoption("--headless", action="store_true", help="headless режим. только в False(по умолчанию) или True")
    parser.addoption("--url", help="URL")
    parser.addoption("--log_level", action="store", default="INFO")


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("--browser")
    drivers_folder = request.config.getoption("--drivers_folder")
    headless = request.config.getoption("--headless")
    url = request.config.getoption("--url")

    log_level = request.config.getoption("--log_level")
    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"tests/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)

    logger.info("===> Test %s started at %s" % (request.node.name, datetime.datetime.now()))

    driver = None
    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument('--headless=new')
        driver = webdriver.Chrome()

    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        if headless:
            options.add_argument('--headless=new')
        service = FirefoxService(executable_path=os.path.join(drivers_folder, "chromedriver"))
        driver = webdriver.Firefox(service=service, options=options)

    elif browser_name == "edge":
        options = webdriver.EdgeOptions()
        if headless:
            options.add_argument('--headless=new')
        service = EdgeService(executable_path=os.path.join(drivers_folder, "msedgedriver"))
        driver = webdriver.Edge(service=service, options=options)

    elif browser_name == "opera":
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument('--headless=new')
        service = ChromeService(executable_path=os.path.join(drivers_folder, "operadriver"))
        driver = webdriver.Chrome(service=service, options=options)

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

    driver.maximize_window()
    driver.get(url)
    yield driver
    driver.quit
    logger.info("===> Test %s finished at %s" % (request.node.name, datetime.datetime.now()))
