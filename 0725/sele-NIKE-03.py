from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
url = 'https://www.nike.com/tw/'
driver.get(url)
driver.maximize_window()
time.sleep(2)

login=driver.find_element(By.XPATH,'//*[@id="gen-nav-commerce-header-v2"]/nav/div[1]/div/div[2]/nav/ul/li[3]/a/p')

login.click()
time.sleep(2)

mail = driver.find_element(By.XPATH, '//*[@id="username"]')
mail.send_keys('@gmail.com')
mail.send_keys(Keys.ENTER)

time.sleep(30)

driver.quit()