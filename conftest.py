import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
import os.path
import logging
import datetime
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="Browser. Default option is chrome")
    parser.addoption("--drivers_folder", default="D:\\drivers\\", help="Path to the drivers")
    parser.addoption("--headless", action="store_true", help="headless режим. только в False(по умолчанию) или True")
    parser.addoption("--url", help="URL")
    parser.addoption("--log_level", action="store", default="INFO")
    parser.addoption("--remote", default=False)
    parser.addoption("--executor", default="localhost")


@pytest.fixture
def base_url(request):
    executor = request.config.getoption("--executor")
    url = f"http://{executor}"
    return url


@pytest.fixture()
def browser(request):
    browser = request.config.getoption("--browser")
    drivers_folder = request.config.getoption("--drivers_folder")
    headless = request.config.getoption("--headless")
    remote = request.config.getoption("--remote")
    executor = request.config.getoption("--executor")

    log_level = request.config.getoption("--log_level")
    logger = logging.getLogger(request.node.name)
    file_handler = logging.FileHandler(f"tests/{request.node.name}.log")
    file_handler.setFormatter(logging.Formatter('%(levelname)s %(message)s'))
    logger.addHandler(file_handler)
    logger.setLevel(level=log_level)
    logger.info("===> Test %s started at %s" % (request.node.name, datetime.datetime.now()))

    if not remote:
        driver = None
        if browser == "chrome":
            options = webdriver.ChromeOptions()
            if headless:
                options.add_argument('--headless=new')
            driver = webdriver.Chrome()

        elif browser == "firefox":
            options = webdriver.FirefoxOptions()
            if headless:
                options.add_argument('--headless=new')
            service = FirefoxService(executable_path=os.path.join(drivers_folder, "chromedriver"))
            driver = webdriver.Firefox(service=service, options=options)

        elif browser == "edge":
            options = webdriver.EdgeOptions()
            if headless:
                options.add_argument('--headless=new')
            service = EdgeService(executable_path=os.path.join(drivers_folder, "msedgedriver"))
            driver = webdriver.Edge(service=service, options=options)

        elif browser == "opera":
            options = webdriver.ChromeOptions()
            if headless:
                options.add_argument('--headless=new')
            service = ChromeService(executable_path=os.path.join(drivers_folder, "operadriver"))
            driver = webdriver.Chrome(service=service, options=options)

    else:
        capabilities = {
            "browserName": browser,
            "acceptInsecureCerts": True,
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            },
        }
        options = Options()
        for k, v in capabilities.items():
            options.set_capability(k, v)
        driver = webdriver.Remote(
            command_executor=f"http://{executor}:4444/wd/hub",
            options=options
        )

    driver.log_level = log_level
    driver.logger = logger
    driver.test_name = request.node.name

    driver.maximize_window()
    driver.get(f"http://{executor}")
    yield driver
    driver.quit
    logger.info("===> Test %s finished at %s" % (request.node.name, datetime.datetime.now()))
