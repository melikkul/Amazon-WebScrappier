from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoSuchWindowException


def seller_count_checker(driver):
    try:
        seller_count_element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'olp-text-box'))
        )
        seller_count_text = seller_count_element.text
        return "Satıcı Sayısı:", seller_count_text[12:14]
    except (NoSuchElementException, TimeoutException):
        return "Satıcı Sayısı: 1"
    except NoSuchWindowException:
        return "Hedef pencere/sekme mevcut değil."
    
    '''
    try:
        seller_count_element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'olp-text-box'))
        )
        seller_count_text = seller_count_element.text
        print("Satıcı Sayısı:", seller_count_text[12:14])
    except (NoSuchElementException, TimeoutException):
        # Element bulunamadıysa veya zaman aşımı olduysa varsayılan değeri kullan
        print("Satıcı Sayısı: 1")
    '''