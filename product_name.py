from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoSuchWindowException


def product_name_checker(driver):
    try:
        product_title = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.ID, 'productTitle'))
        )
        return "Ürün adı: " + product_title.text
    except (NoSuchElementException, TimeoutException):
        return None
    except NoSuchWindowException:
        return "Hedef pencere/sekme mevcut değil."
    
    '''try:
        product_title = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.ID, 'productTitle'))
        )
        print("Ürün adı:", product_title.text)
    except (NoSuchElementException, TimeoutException):
        print("Ürün adı bulunamadı.")
    '''