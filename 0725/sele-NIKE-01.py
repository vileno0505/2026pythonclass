from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url = 'https://www.nike.com/tw/w/sale-3yaep'
driver.get(url)
driver.maximize_window()
time.sleep(2)

products = driver.find_elements(By.CLASS_NAME, 'product-card__body')
# print(titles)
for product in products:
    title = product.find_element(By.CLASS_NAME, 'product-card__title').text
    price = product.find_element(By.CLASS_NAME, 'is--current-price').text
# is--current-price
    print(f'商品名稱:{title} \n 目前售價:{price}')
    print('*'*30)

time.sleep(2)

driver.quit()