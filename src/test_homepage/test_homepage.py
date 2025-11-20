from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

class TestHomepage:
    """Homepage test ui elements

    Returns:
        Object
    """
    url: str
    driver: WebDriver

    def setup_method(self):
        """setup class variables to test homepage
        """
        chrome_options = Options()

        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--window-size=1920,1080")

        self.driver = webdriver.Chrome(options=chrome_options)
        self.url = "https://icb-web.vercel.app/home"
        self.driver.get(self.url)

    def test_page_is_accessible(self):
        """Test if homepage is accessible

        Returns:
            None
        """
        xpath_chess_piece_image = "//img[@alt= 'Chess Piece']"
        chess_piece_image = self.driver.find_element(By.XPATH, xpath_chess_piece_image)
        assert chess_piece_image is not None, "Test Failed (Homepage): page is not accessible"

    def teardown_method(self):
        self.driver.quit()
