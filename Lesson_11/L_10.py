# Постановка задачи
#
# Открыть сайт https://test.sbis.ru  -  URL, title
# Найти элемент: кнопка «Начать работать»  -  текст, title, отображение
# Кликнуть на кнопку  -  открылась вторая вкладка, url,   title
# Авторизоваться  -  Перешли в лк
# Имитировать наведение мышкой на новость, контекстный клик  -  Открылось контекстное меню

from selenium import webdriver
from time import sleep

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
sbis_site = 'https://test.sbis.ru/'
sbis_title = 'СБИС — экосистема для бизнеса: учет, управление и коммуникации'

try:
    driver.get(sbis_site)
    sleep(1)
    print('Проверить адрес сайта и заголовок страницы')
    assert driver.current_url == sbis_site, 'Неверный адрес сайта'
    assert driver.title == sbis_title, 'Неверный заголовок сайта'

    print('Проверить отображение четырех вкладок')
    tabs = driver.find_elements(By.CSS_SELECTOR, '.sbisru-Header__menu-item')
    assert len(tabs) == 4

    print('Проверить текст, атрибут и видимость кнопки Начать работу')
    button_txt = 'Начать работу'
    start_btn = driver.find_element(By.CSS_SELECTOR, '.sbisru-Button--primary')
    assert start_btn.text == button_txt
    assert start_btn.get_attribute('title') == button_txt

    print('Перейти на страницу авторизации')
    assert start_btn.is_displayed(), 'Элемент не отображается'
    start_btn.click()
    driver.switch_to.window(driver.window_handles[1])

    print('Проверить адрес сайта и заголовок страницы')
    assert 'test-online.sbis.ru' in driver.current_url
    assert driver.title == 'Вход в личный кабинет'

    print('Авторизоваться')
    sleep(1)
    user_login, user_password = 'discus_admin1', 'discus_admin123'
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys(user_login, Keys.ENTER)
    assert login.get_attribute('value') == user_login
    sleep(1)
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys(user_password, Keys.ENTER)

    print('Навести курсор на новость и сделать контекстный клик')
    sleep(3)
    news = driver.find_elements(By.CSS_SELECTOR, '.feed-Title')
    news_item = news[2]
    action_chains = ActionChains(driver)
    action_chains.move_to_element(news_item)
    action_chains.context_click(news_item)
    action_chains.perform()

    print('Проверить отображение контекстного меню')
    popup = driver.find_element(By.CSS_SELECTOR, '[templatename="Controls/menu:Popup"]')
    assert popup.is_displayed(), 'Контекстное меню не отображается'
finally:
    driver.quit()