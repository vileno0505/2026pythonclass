from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url = 'https://www.apple.com/tw/shop/refurbished/mac'
driver.get(url)
driver.maximize_window()

time.sleep(2)

products = driver.find_elements(By.CLASS_NAME,'rf-refurb-producttile')

for product in products:
    print(product.text)

driver.find_element(By.XPATH,'//*[@id="root"]/div/nav/div/div[3]/button').click()

time.sleep(3)

products2 = driver.find_elements(By.CLASS_NAME,'rf-refurb-producttile')

for product2 in products2:
    print(product2.text)

driver.quit()
