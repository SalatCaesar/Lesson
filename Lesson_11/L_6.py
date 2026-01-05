from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()
sbis_site = 'https://sbis.ru/'
try:
    sleep(1)
    browser.execute_script("alert('Robots at work');")

    sleep(5)

finally:
    browser.quit()