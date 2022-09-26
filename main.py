from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import requests
import pandas as pd

class MainApp:

    def __init__(self, driver, page_atack) -> None:
        self.path       = driver        
        self.page_atack = page_atack    
        self.drivers    = webdriver.Chrome(self.path)
        self.drivers.get(self.page_atack)

    def Event_click_Button(self, btn_click):
        WebDriverWait(self.drivers, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, btn_click))
        ).click()

    def SearchSomething(self, data_search, element):
        WebDriverWait(self.drivers, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, element))
        ).send_keys(data_search)

    def CatchData(self, element_html, data_element_html):
        url_catch = self.drivers.current_url
        page = requests.get(url_catch)
        soup = BeautifulSoup(page.content, 'html.parser')

        res =soup.find_all(element_html, class_=data_element_html)

        data_cath_scrab = list()
        count = 1

        for i in res:
            # 'id: ' + str(count) +
            data_cath_scrab.append(i.text)
            count += 1

        return data_cath_scrab

    def ApendDataCatch():
        pass
    

if __name__ == '__main__':
    # C:\\Users\\usuario\\Desktop\\scrap\\assets\\chromedriver.exe
    start = MainApp('assets/chromedriver.exe', 'https://www.mercadolibre.com.ec/')
    start.Event_click_Button('button.cookie-consent-banner-opt-out__action')
    start.SearchSomething('termos', 'input.nav-search-input')
    start.Event_click_Button('button.nav-search-btn')
    res_catch_prod  = start.CatchData('h2',     'ui-search-item__title')    
    res_catch_price = start.CatchData('span',   'price-tag-fraction')    
    count   = 0
    xcount  = 1
    for i in res_catch_prod:        
        count += 1
        if count%2:
            res_catch_prod.insert(count, res_catch_price[xcount])
            xcount += 1

    print(res_catch_prod)
    print(res_catch_price)

    df = pd.DataFrame({'Producto': res_catch_prod})
    print('***********************df***********************')
    print(df)
    print('***********************df***********************')
