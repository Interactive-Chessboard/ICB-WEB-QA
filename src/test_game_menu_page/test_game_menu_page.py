from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from utils import utils
import selenium
import os
from dotenv import load_dotenv
import time

class TestGameMenuPage:
    driver:WebDriver
    url:str

    def setup_method(self):
        """setup class variables to test game menu page"""
        chrome_options = Options()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")

        self.driver = webdriver.Chrome(chrome_options)
        self.url = "https://icb-web.vercel.app/menu"
        self.driver.get(self.url)

        # Ouath Login
        self.wait_for_login_page()
        self.login()
        self.wait_for_cookies_page()
        self.wait_for_authorize_button()
        self.accept_cookies()
        time.sleep(5)

    def test_page_is_accessible(self):
        try:
            home_nav_item_text_xpath = "//h1[normalize-space() = 'Home']"
            home_nav_item_text = self.driver.find_element(By.XPATH, home_nav_item_text_xpath)
            assert home_nav_item_text is not None, "Test Failed(Game Menu Page): Page is not accessible"
        except selenium.common.exceptions.NoSuchElementException:
            assert False, "Test Failed(Game Menu Page): Page is not accessible"

    def wait_for_login_page(self):
        """Check if the signIn page is visible on screen

        Returns:
            bool: True if visible on screen
        """
        sign_in_text_xpath = "//h1[normalize-space() = 'Sign in']"
        utils.wait_for(self.driver, By.XPATH, sign_in_text_xpath)

    def wait_for_cookies_page(self):
        authorize_text_xpath = "//h1[normalize-space() = 'Authorize']"
        utils.wait_for(self.driver,By.XPATH,authorize_text_xpath)

    def wait_for_authorize_button(self):
        authorize_button_id = "oauth-authorize"
        utils.wait_for_button_clickable(self.driver, By.ID, authorize_button_id)

    def login(self):
        """Login with the lichess account
        """
        username_input_id = "form3-username"
        username_input = self.driver.find_element(By.ID, username_input_id)

        password_input_id = "form3-password"
        password_input = self.driver.find_element(By.ID, password_input_id)

        login_button_xpath = "//button[normalize-space() = 'Sign in']"
        login_button = self.driver.find_element(By.XPATH, login_button_xpath)

        load_dotenv()
        username = os.getenv("LICHESS_USERNAME")
        password = os.getenv("LICHESS_PASSWORD")

        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button.click()

    def accept_cookies(self):
        """Accespt ouath cookies"""
        authorize_button_id = "oauth-authorize"
        authorize_button = self.driver.find_element(By.ID, authorize_button_id)
        authorize_button.click()

    def teardown_method(self):
        self.driver.quit()
