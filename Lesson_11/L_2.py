from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
try:
    browser.get('https://sbis.ru')

    header = browser.find_element(By.CSS_SELECTOR, '.sbisru-Main-banner-img')

finally:
    browser.close()