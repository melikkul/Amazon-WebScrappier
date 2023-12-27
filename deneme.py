'''from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

#Excel Yolu
excel_path = 'D:/ASIN_10000.xlsx'
df = pd.read_excel(excel_path)

# ChromeDriver yolu
driver_path = 'D:/KODLAMA/PYTHON/Amazon WebScrappier/chromedriver.exe'
service = webdriver.ChromeService(executable_path=driver_path)

# WebDriver'ı başlat
driver = webdriver.Chrome()

Amazon_base_link = 'https://www.amazon.com/dp/'

for asin in df['ASIN']:
    url = Amazon_base_link + asin

    # Amazon ürün sayfasını aç
    driver.get(url)
    driver.maximize_window()

    time.sleep(20)
    a = 0

    # Lokasyonu kontrol et
    try:
        element = driver.find_element(By.ID, 'glow-ingress-line2').text
        zipcode_buton = driver.find_element(By.ID, 'nav-global-location-popover-link')
        if element == "Turkey":
            zipcode_buton.click()
            input("Lütfen lokasyonu değiştirin!! Değiştirdikten sonra işleme devam etmek için Enter'a bas...")
    except NoSuchElementException:
        print("Lokasyon bilgisi bulunamadı.")

    # Fiyat ve diğer bilgileri al
    try:
        product_price = driver.find_element(By.CLASS_NAME, 'a-price-whole').text
        product_price2 = driver.find_element(By.CLASS_NAME, 'a-price-fraction').text
        combined_price = product_price + "." + product_price2
        print("Ürün Fiyatı:", combined_price)
    except NoSuchElementException:
        print("Ürün fiyatı bulunamadı.")
        continue

    try:
        product_title = driver.find_element(By.ID, 'productTitle').text
        print("Ürün adı:", product_title)
    except NoSuchElementException:
        print("Ürün adı bulunamadı.")

    try:
        seller_count = driver.find_element(By.CLASS_NAME, 'olp-text-box').text
        print("Satıcı Sayısı:", seller_count[12:14])
    except NoSuchElementException:
        print("Satıcı Sayısı : 1")


    # Kullanıcı girişi bekleniyor
    #input("Sayfa açık kalmaya devam ediyor. Devam etmek için Enter'a basın...")

# WebDriver'ı kapat
driver.quit()
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

# Excel Yolu
excel_path = 'D:/ASIN_10000.xlsx'
df = pd.read_excel(excel_path)

# ChromeDriver yolu
driver_path = 'D:/KODLAMA/PYTHON/Amazon WebScrappier/chromedriver.exe'
service = webdriver.ChromeService(executable_path=driver_path)

# WebDriver'ı başlat
driver = webdriver.Chrome()

Amazon_base_link = 'https://www.amazon.com/dp/'

for asin in df['ASIN']:
    url = Amazon_base_link + asin

    # Amazon ürün sayfasını aç
    driver.get(url)
    driver.maximize_window()

    # Lokasyonu kontrol et
    try:
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

    # Fiyat ve diğer bilgileri al
    try:
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

    try:
        product_title = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.ID, 'productTitle'))
        )
        print("Ürün adı:", product_title.text)
    except (NoSuchElementException, TimeoutException):
        print("Ürün adı bulunamadı.")

    try:
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

    try:
        seller_count_element = WebDriverWait(driver, 2).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'olp-text-box'))
        )
        seller_count_text = seller_count_element.text
        print("Satıcı Sayısı:", seller_count_text[12:14])
    except (NoSuchElementException, TimeoutException):
        # Element bulunamadıysa veya zaman aşımı olduysa varsayılan değeri kullan
        print("Satıcı Sayısı: 1")





# WebDriver'ı kapat
driver.quit()
