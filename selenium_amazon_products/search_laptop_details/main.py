#scraping multiple laptop details after inputting a search term in amazon.com

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from openpyxl import Workbook


from src import SEARCH_URL
from src import (
    config_driver,scrape_page, get_next_page
    )


def main():
    
    wb = Workbook()
    ws = wb.active

    headers = ['Link', 'Title', 'Price ($)', 'Brand', 'Model Name', 'Screen Size', 'About this item',
               'Technical details: Summary', 'Rating (out of 5)']
    ws.append(headers)
    
    page=1
    while True:
        print(f"Page: {page}")
        driver = config_driver()
        driver.get(SEARCH_URL)
    
        scrape_page(driver, ws)
        
        # if not get_next_page(driver):
        #     break
        page=page+1
            

    wb.save('./data/laptop_details1.xlsx')
    

if __name__ == "__main__":
    main()