from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoSuchWindowException


def seller_type_checker(driver):
    try:
        seller_type = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.ID, 'fulfillerInfoFeature_feature_div'))
        )
        seller_name = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.ID, 'sellerProfileTriggerId'))
        )

        if seller_type.text[11:] == seller_name.text:
            return "Satıcı Türü : FBM"
        else:
            return "Satıcı Türüne Erişilemedi!!"

    except (NoSuchElementException, TimeoutException):
        return "Satıcı Türü : FBA"
    except NoSuchWindowException:
        return "Hedef pencere/sekme mevcut değil."


    '''try:
        seller_type = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.ID, 'fulfillerInfoFeature_feature_div'))
        )
        seller_name = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.ID, 'sellerProfileTriggerId'))
        )

        if seller_type.text[11:] == seller_name.text:
            print("Satıcı Türü : FBM")
        else:
            # Ekstra debug: if bloğuna girmediğinde bunu yazdır
            print("Metinler eşleşmiyor.")

    except (NoSuchElementException, TimeoutException):
        print("Satıcı Türü : FBA")
    '''