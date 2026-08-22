from selenium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://www.ptt.cc/bbs/NBA/index.html")
time.sleep(1)
search=driver.find_element(By.CLASS_NAME,'query')
search.send_keys('L')
time.sleep(0.12)
search.send_keys('B')
time.sleep(0.232)
search.send_keys('J')
time.sleep(0.65)

search.send_keys(Keys.ENTER)

time.sleep(10)

driver.quit()