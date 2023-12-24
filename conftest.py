import pytest
from selenium import webdriver
import logging
import datetime
from selenium.webdriver.chrome.options import Options
import paramiko


def pytest_addoption(parser):
    parser.addoption("--browser", default="chrome", help="Browser. Default option is chrome")
    parser.addoption("--headless", action="store_true", help="headless режим. только в False(по умолчанию) или True")
    parser.addoption("--url", help="URL")
    parser.addoption("--log_level", action="store", default="INFO")
    parser.addoption("--remote", default=False)
    parser.addoption("--executor", default="localhost")
    parser.addoption("--user", help="username for remote virtual machine")
    parser.addoption("--password", help="password for remote virtual machine")


@pytest.fixture()
def browser(request):
    browser = request.config.getoption("--browser")
    headless = request.config.getoption("--headless")
    remote = request.config.getoption("--remote")
    executor = request.config.getoption("--executor")
    user = request.config.getoption("--user")  # only for remote start
    password = request.config.getoption("--password")  # only for remote start

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
            driver = webdriver.Firefox(options=options)

        elif browser == "edge":
            options = webdriver.EdgeOptions()
            if headless:
                options.add_argument('--headless=new')
            driver = webdriver.Edge(options=options)

        elif browser == "opera":
            options = webdriver.ChromeOptions()
            if headless:
                options.add_argument('--headless=new')
            driver = webdriver.Chrome(options=options)

    else:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(f'{executor}', username=f'{user}', password=f'{password}')

        capabilities = {
            "browserName": browser,
            "acceptInsecureCerts": True,
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": False
            }
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
    if remote:
        ssh.close()
    logger.info("===> Test %s finished at %s" % (request.node.name, datetime.datetime.now()))


@pytest.fixture
def base_url(request):
    remote = request.config.getoption("--remote")
    executor = request.config.getoption("--executor")
    if remote:
        url = f"http://{executor}"
    else:
        url = "http://localhost"
    return url

# второй вариант вместо фикстуры base_url: в фикстуре browser прописать yield driver, base_url - Передача нескольких
# переменных через yield (browser = tuple(кортеж)), потом в каждом тесте из фикстуры нужно будет получать неск. значений
# (def test4_admin_page(browser):
# browser, base_url = browser
# browser.get(f"{base_url}/admin"))
# но тогда тоже получится избыточный код, потому что не в каждом тесте нужен base_url
