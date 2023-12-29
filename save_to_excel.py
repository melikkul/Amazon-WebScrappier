import pandas as pd

def save_to_excel_func(data, columns):
    if data[0] != "Ürün bulunamadı!":
        df = pd.DataFrame(data, columns=columns)
        df.to_excel('ASIN_Results.xlsx', index=False)