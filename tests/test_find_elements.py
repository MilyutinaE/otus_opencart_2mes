from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def test1_main_page(browser):
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    assert wait.until(EC.title_is("Your Store"))
    assert wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Featured']")))
    assert wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@class='carousel swiper-viewport']")))
    assert wait.until(EC.visibility_of_element_located((By.ID, "content")))
    assert wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".nav.navbar-nav")))   # class="nav navbar-nav"


def test2_catalog_page(browser):
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()='MP3 Players']"))).click()
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Show All MP3 Players']"))).click()
    assert wait.until(EC.title_is("MP3 Players"))
    category = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@class='list-group-item active']"))).text
    assert "MP3 Players" in category   # проверяем, что в названии категории слева есть MP3 Players
    assert wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".product-thumb")))
    assert wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".price")))
    assert wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Add to Cart']")))


def test3_product_page(browser):
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    browser.get("http://192.168.0.114:8081/camera/canon-eos-5d")
    assert wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@class='list-unstyled']//*[contains(text(),"
                                                                  " 'Availability:')]")))  # есть доступность
    assert wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@class='list-unstyled']//*[contains(text(),"
                                                                  " 'Product Code:')]")))  # есть код продукта
    assert wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@class='list-unstyled']//*[contains(text(),"
                                                                  " 'Brand:')]")))  # есть изготовитель
    assert wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Add to Cart']")))
    assert wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Description']")))


def test4_admin_page(browser):
    browser.get("http://192.168.0.114:8081/admin/")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    assert wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@name='username']")))
    assert wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@name='password']")))
    assert wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@class='help-block']")))
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-primary"))).click()
    assert wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@class='help-block']/a"))).click()
    assert wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@name='email']")))


def test5_register_page(browser):
    browser.get("http://192.168.0.114:8081/index.php?route=account/register")
    wait = WebDriverWait(browser, 10, poll_frequency=1)
    assert wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@name='firstname']")))
    assert wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@name='lastname']")))
    assert wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@name='email']")))
    assert wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@type='checkbox'  and @value='1']")))  # чекбокс
    wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@type='submit']"))).click()
    assert wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
