import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

workbook=openpyxl.Workbook() #開啟excel
sheet=workbook.active #啟動工作表

url = 'https://www.apple.com/tw/shop/refurbished/mac'
driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()

#做一個資料儲存區存放等等每一個分頁的商品資料
all_products = []

#抓取商品名稱及價格
#因apple的網頁設計換頁時網址不會變，所以資料存取時會發生錯誤存不進去all_products裡，必須寫迴圈
while True:
    products = driver.find_elements(By.CLASS_NAME, 'rf-refurb-producttile')
    for product in products:
        title = product.find_element(By.CLASS_NAME, 'rf-refurb-producttile-link').text
        price = product.find_element(By.CSS_SELECTOR, 'span.rf-refurb-producttile-currentprice').text

#建立一個字典
        p = {}
        p['title'] = title
        p['price'] = price
#把字典裡的資料存入all_products
        all_products.append(p)

#當下一頁無法再按時，檢視按鈕，原始碼會出現disable，表示是最後一頁了(此網站為例)
#將disable出現的時候設為資料抓取的終點
#btn的按鍵如果不會換位置才能使用xpath去抓
    btn = driver.find_element(By.XPATH, '//*[@id="root"]/div/nav/div/div[3]/button')
    if btn.get_attribute('disabled'):
        break
    btn.click()

    time.sleep(2)

#開始印出檔案
print(f'共找到{len(all_products)}筆整修品')

#將字典中的資料以迴圈繞出
for product in all_products:
    print(f'商品名稱：{product['title']}')
    print(f'價格：{product['price']}')
    print('*' * 100)

    sheet.append([product['title'], product['price']])
    # 將資料存成串列，for每繞一圈存一次

driver.quit()



workbook.save('APPLE整修品.xlsx')  # excel存檔