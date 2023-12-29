from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoSuchWindowException


def price_check_func(driver):
    try:
        product_price = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'a-price-whole'))
        )
        product_price2 = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'a-price-fraction'))
        )
        combined_price = product_price.text + "." + product_price2.text
        return combined_price
    except (NoSuchElementException, TimeoutException):
        return "Ürün bulunamadı!"
    except NoSuchWindowException:
        return "Hedef pencere/sekme mevcut değil."
    

    '''try:
        product_price = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'a-price-whole'))
        )
        product_price2 = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'a-price-fraction'))
        )
        combined_price = product_price.text + "." + product_price2.text
        print("Ürün Fiyatı:", combined_price)
    except (NoSuchElementException, TimeoutException):
        continue
    '''