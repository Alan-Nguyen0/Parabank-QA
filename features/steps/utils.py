from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

def page_loaded(driver, element, wait):
    try:
        element_present = EC.presence_of_element_located((By.XPATH, element))
        WebDriverWait(driver, wait).until(element_present)
        return True
    except TimeoutException:
        print("Timed out waiting for page to load")
        return False