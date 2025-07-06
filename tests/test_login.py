# tests/test_login.py

import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage

def test_successful_login():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), 
        options=chrome_options
    )

    driver.get("https://para.testar.org/parabank/index.htm")
    driver.implicitly_wait(5)

    login_page = LoginPage(driver)

    login_page.enter_username("john")
    login_page.enter_password("demo")
    login_page.click_login_button()

    try:
        wait = WebDriverWait(driver, 10)
        accounts_overview_title = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//h1[text()='Accounts Overview']"))
        )
        assert accounts_overview_title.is_displayed()
    except TimeoutException:
        pytest.fail("The title 'Accounts Overview' was not found. Possibly login failed.")
    finally:
        driver.quit()
