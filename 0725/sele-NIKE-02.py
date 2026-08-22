from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url = 'https://www.nike.com/tw/w/sale-3yaep'
driver.get(url)
driver.maximize_window()

time.sleep(2)

#先捲出所有品項之後再開始蒐集全部資料
#利用迴圈讓網頁捲動(因不知道需要捲幾次，所以使用while迴圈
count = 0
while True:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight - 1500)")
    time.sleep(2)
    products = driver.find_elements(By.CLASS_NAME, 'product-card__body')
    print(len(products))
    if len(products) == count:
        break
    count = len(products)
    #用len計算商品品項總量，當迴圈捲出來的品項數量=總量時，表示捲到底了，就可以把迴圈break掉


products = driver.find_elements(By.CLASS_NAME, 'product-card__body')
for product in products:
    title = product.find_element(By.CLASS_NAME, 'product-card__title').text
    price = product.find_element(By.CLASS_NAME, 'is--current-price').text
    print(f'商品名稱:{title} \n 目前售價:{price}')
    print('*' * 30)


time.sleep(2)

driver.quit()
