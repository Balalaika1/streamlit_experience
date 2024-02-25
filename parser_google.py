from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

def selen_func():
    chrome_driver_path = "./chromedriver"

    #@st.cache_resource
    def get_driver():
        return webdriver.Chrome(ChromeDriverManager().install())(options=options)



    options = Options()
    options.add_argument('--disable-gpu')
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    driver = get_driver()
    
    #try:
    #    driver.quit()
    #except:
    #    st.write("good quit")

    try:
        driver.get("https://hh.ru/account/login?customDomain=1")
        sleep(5)
        print(1)
        st.write("Scraper activation (preparation for scraping 1/5)")
    except:
        st.write("1/5-non")
    data = driver.page_source
    driver.quit()
    soup = BeautifulSoup(data, 'html.parser')
    span_element = soup.find('span', class_='ktLKi')

    if span_element:
        text = span_element.get_text()
    else:
        text = "Элемент не найден."
    return text

