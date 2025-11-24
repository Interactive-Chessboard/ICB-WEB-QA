from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for(driver,by, value, timeout = 10):
        """Helper method to wait for a specefic element 

        Args:
            by (_type_): _description_
            value (_type_): _description_
            timeout (int, optional): _description_. Defaults to 10.
        """
        return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))

def wait_for_button_clickable(driver, by, value, timeout = 10):
    """Helper method to wait for a specefic element 

        Args:
            by (_type_): _description_
            value (_type_): _description_
            timeout (int, optional): _description_. Defaults to 10.
    """
    return WebDriverWait(driver,timeout).until(EC.element_to_be_clickable((by, value)))