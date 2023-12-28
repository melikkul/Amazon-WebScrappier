from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoSuchWindowException

def check_and_change_location(driver):
    try:
        element = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, 'glow-ingress-line2'))
        )
        zipcode_buton = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.ID, 'nav-global-location-popover-link'))
        )
        if element.text == "Turkey":
            zipcode_buton.click()
            input("Lütfen lokasyonu değiştirin!! Değiştirdikten sonra işleme devam etmek için Enter'a bas...")
    except (NoSuchElementException, TimeoutException):
        pass  # 'next' yerine 'pass' kullanılır
    except NoSuchWindowException:
        return "Hedef pencere/sekme mevcut değil."


    '''try:
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, 'glow-ingress-line2'))
        )
        zipcode_buton = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'nav-global-location-popover-link'))
        )
        if element.text == "Turkey":
            zipcode_buton.click()
            input("Lütfen lokasyonu değiştirin!! Değiştirdikten sonra işleme devam etmek için Enter'a bas...")
    except (NoSuchElementException, TimeoutException):
        next
    '''