import selenium
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

class TestShop:
    """Test shop page ui elements
    
    Returns:
        Object
    """
    url:str
    driver: WebDriver

    def setup_method(self):
        """setup class variables"""
        chrome_options = Options()

        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--window-size=1920,1080")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.url = "https://icb-web.vercel.app/shop"
        self.driver.get(self.url)

    def test_page_is_accessible(self):
        """Test if shop is accessible
        Returns:
            None"""
        xpath_collection_text = "//div[normalize-space() = 'Collection']"
        try:
            element = self.driver.find_element(By.XPATH, xpath_collection_text)
            assert element is not None, "Test Failed (Shop): page is not accessible"
        except selenium.common.exceptions.NoSuchElementException:
            assert False, "Test Failed (Shop): page is not accessible"

    def test_is_classic_walnut_board_listed(self):
        """Test if classic board is listed in the shop
        """
        xpath_classic_walnut_board = "//h2[normalize-space() = 'Classic Walnut']"

        try:
            element = self.driver.find_element(By.XPATH, xpath_classic_walnut_board)
            assert element is not None, "Test Failed (Shop): classic walnut board is not listed in shop"
        except selenium.common.exceptions.NoSuchElementException:
            assert False, "Test Failed (Shop): classic walnut board is not listed in shop"

    def test_is_marble_deluxe_board_listed(self):
        """Test if marble board is listed in the shop
        """
        xpath_marble_deluxe_board = "//h2[normalize-space() = 'Marble Deluxe']"

        try:
            element = self.driver.find_element(By.XPATH, xpath_marble_deluxe_board)
            assert element is not None, "Test Failed (Shop): marble deluxe board is not listed in shop"
        except selenium.common.exceptions.NoSuchElementException:
            assert False, "Test Failed (Shop): marble deluxe board is not listed in shop"

    def test_is_portable_folding_board_listed(self):
        """Test if portable folding is listed in the shop
        """
        xpath_portable_folding_board = "//h2[normalize-space() = 'Portable Folding']"

        try:
            element = self.driver.find_element(By.XPATH, xpath_portable_folding_board)
            assert element is not None, "Test Failed (Shop): portable folding board is not listed in shop"
        except selenium.common.exceptions.NoSuchElementException:
            assert False, "Test Failed (Shop): marble portable folding is not listed in shop"

    def teardown_method(self):
        self.driver.quit()
