import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_user_must_see_browser_with_option_language(browser):
    browser.get(link)
    time.sleep(30)
    # checking present the add-to-cart(button) on the page
    button = WebDriverWait(browser, 10).until(EC.visibility_of_element_located(
        (By.CSS_SELECTOR, 'button.btn-add-to-basket')))
    assert button, 'button add to cart - is absent'
