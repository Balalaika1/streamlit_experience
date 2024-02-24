from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def selen_func():
    sites = 'http://google.com'
    random_site = sites

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)

    # Переместили открытие сайта перед вызовом driver.quit()
    driver.get(random_site)

    # Получаем исходный код страницы до закрытия драйвера
    data = driver.page_source

    # Теперь можно безопасно закрыть драйвер
    driver.quit()

    # Создание объекта BeautifulSoup происходит после получения данных
    soup = BeautifulSoup(data, 'html.parser')
    span_element = soup.find('span', class_='ktLKi')

    if span_element:
        text = span_element.get_text()

    else:
        text = "Элемент не найден."
    return text
