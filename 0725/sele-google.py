from selenium import webdriver
import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://www.google.com/?hl=zh_TW")
time.sleep(1)
search=driver.find_element(By.CLASS_NAME,'gLFyf')
search.send_keys('h')
time.sleep(0.12)
search.send_keys('e')
time.sleep(0.232)
search.send_keys('l')
time.sleep(0.4)
search.send_keys('l')
time.sleep(0.25)
search.send_keys('o')
time.sleep(0.65)

search.send_keys(Keys.ENTER)

driver.save_screenshot('test.png')

driver.quit()