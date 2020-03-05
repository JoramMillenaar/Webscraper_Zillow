import os
from time import sleep
from selenium import webdriver
BASE_DIR = os.path.join(os.getcwd(), 'RealEstate')

def scrape_zillow(xpath):
    ''' Scrapes Zillow's homepage houses information'''
    url = 'https://www.zillow.com/redding-ca/'
    list_pos = 1
    data = []
    browser = webdriver.Safari()
    sleep(2)
    browser.get(url)
    sleep(8)

    while True:
        xpath_list = f'{xpath}[{list_pos}]'
        try:
            element = browser.find_element_by_xpath(xpath_list)
            data.append({
                'text': element.text,
                'data': element.get_attribute('innerHTML')
            })
            list_pos += 1
        except IndexError:
            break
    browser.quit()
    print(data)
    return data