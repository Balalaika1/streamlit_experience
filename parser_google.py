from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def selen_func():
    sites = 'http://google.com'
    random_site = sites

    # Создаем объект опций для Chrome
    options = Options()
    options.add_argument("--headless")  # Запуск браузера без GUI
    options.add_argument("--no-sandbox")  # Обход режима песочницы
    options.add_argument("--disable-dev-shm-usage")  # Отключение использования /dev/shm
    options.add_argument("--disable-gpu")  # Отключение аппаратного ускорения
    options.add_argument("--disable-features=NetworkService")  # Отключение NetworkService
    options.add_argument("--window-size=1920x1080")  # Установка размера окна
    options.add_argument("--disable-features=VizDisplayCompositor")  # Отключение VizDisplayCompositor

    # Инициализация драйвера с учетом опций
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    driver.get(random_site)
    data = driver.page_source
    driver.quit()

    soup = BeautifulSoup(data, 'html.parser')
    span_element = soup.find('span', class_='ktLKi')

    if span_element:
        text = span_element.get_text()
    else:
        text = "Элемент не найден."
    return text
