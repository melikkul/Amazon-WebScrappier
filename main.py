from selenium import webdriver
import pandas as pd
from selenium.common.exceptions import NoSuchWindowException
from save_to_excel import save_to_excel_func

#############!!FUNCTIONS!!############################
from location_checker import check_and_change_location
from price_checker import price_check_func
from product_name import product_name_checker
from seller_type import seller_type_checker
from seller_count import seller_count_checker
##########################################################

# Excel Yolu
excel_path = 'D:/ASIN_10000.xlsx'
df = pd.read_excel(excel_path)

# ChromeDriver yolu
driver_path = 'D:/KODLAMA/PYTHON/Amazon WebScrappier/chromedriver.exe'
service = webdriver.ChromeService(executable_path=driver_path)

# WebDriver'ı başlat
driver = webdriver.Chrome()


Amazon_base_link = 'https://www.amazon.com/dp/'

########FLGAS################
window_closed_flag = False
location_checked = False
################################

count = 1

data = []

for asin in df['ASIN']:

    try:
        url = Amazon_base_link + asin
        driver.get(url)  # Sayfayı yükle
        driver.set_window_size(1920, 1080)

        # ... (Diğer işlemler)

    
    except NoSuchWindowException:
        print("Hedef pencere/sekme mevcut değil.")
        break  # Veya başka bir uygun işlem yap
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
        continue

    # Lokasyonu kontrol et
    if not location_checked:
            location_status = check_and_change_location(driver)
            if location_status == "Hedef pencere/sekme mevcut değil.":
                print(location_status)
                window_closed_flag = True
                break
            location_checked = True 

    # Fiyat ve diğer bilgileri al
    price_inf = price_check_func(driver)

    if price_inf == "Ürün bulunamadı!":
        print("Ürün bulunamadı, diğer sayfa yükleniyor...")
        continue  # Döngünün başına dön

    print("Ürün Fiyatı: " + price_inf)
    if price_inf == "Hedef pencere/sekme mevcut değil.":
        
        window_closed_flag = True
        break     

    #Ürün ASIN numarası Çekme
    print("Ürün ASIN: " + asin)


    # Ürün Adı verisine erişme
    print("Ürün adı: " + product_name_checker(driver))
    if product_name_checker(driver) == "Hedef pencere/sekme mevcut değil.":
        window_closed_flag = True
        break 
    
    # Satıcı Türü Çekme
    print("Satıcı Türü : " + seller_type_checker(driver))
    if seller_type_checker(driver) == "Hedef pencere/sekme mevcut değil.":
        window_closed_flag = True
        break 

    #Satıcı Sayısı Çekme

    print("Satıcı Sayısı: " + seller_count_checker(driver))
    if seller_count_checker(driver) == "Hedef pencere/sekme mevcut değil.":
        window_closed_flag = True
        break


    # Veri toplama işlemleri...
    product_name = product_name_checker(driver)
    price = price_check_func(driver)
    seller_type = seller_type_checker(driver)
    seller_count = seller_count_checker(driver)

    columns = ['Sayı','Ürün Adı', 'ASIN', 'Fiyat', 'Satıcı Türü', 'Satıcı Sayısı']

    # Sadece geçerli verileri Excel'e ekle
    if price != "Ürün bulunamadı!":
        data.append([count, product_name, asin, price, seller_type, seller_count])
        save_to_excel_func(data, columns)
        print("Excele Başarıyla aktarıldı") 
        count += 1



# WebDriver'ı kapat
driver.quit()
