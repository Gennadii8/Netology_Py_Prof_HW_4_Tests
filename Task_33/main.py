from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os


geckodriver_path = os.path.join(os.getcwd(), 'geckodriver.exe')

driver = webdriver.Firefox(executable_path=geckodriver_path)
driver.get('https://passport.yandex.ru/auth/')
email = driver.find_element_by_id('passp-field-login')
email.send_keys('Tururu')
sleep(1)
email.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
sleep(1)
password = driver.find_element_by_id('passp-field-passwd')
password.send_keys('RAtata')
sleep(1)
eye = driver.find_element_by_css_selector("[type=button]").click()
sleep(1)
password.send_keys(Keys.RETURN)
sleep(1.5)
driver.close()
driver.quit()
