# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 10:31:43 2023

@author: Pradymna_Badave
"""

import logging
import time
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(level=logging.INFO)

searched_importer=[]
shipper=[]
consignee=[]
notify_party=[]
lading_no=[]


def get_info(companies):
    """
    

    Parameters
    ----------
    companies : List
        List of componies want to search.

    Returns
    -------
    df : data frame 
        CSV file which contains shipper,Searched importer,consignee,notify_party,lading_no etc.

    """
    with webdriver.Chrome() as browser:
        browser.get('https://portexaminer.com/')

        for company in companies:
            # select the search field and enter the company name
            drop_down = browser.find_element("name", "search-field-1")
            dd = Select(drop_down)
            dd.select_by_index(1)

            search_bar = browser.find_element("id", "input-box")
            search_bar.clear()  # clear the search bar before entering a new company name
            search_bar.send_keys(company)
            search_bar.send_keys(Keys.RETURN)

            # get the search results
            search_links = [link.get_attribute("href") for item in browser.find_elements(By.CSS_SELECTOR, "div.search-item") for link in item.find_elements(By.TAG_NAME, "a")]

            for url in search_links:
                logging.info(f"Processing link: {url}")
                browser.get(url)
                browser.set_page_load_timeout(30)

                time.sleep(2) # add a delay to wait for page to fully load

                wait = WebDriverWait(browser, 10)
                try:
                    element_head = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[id='shipper'] h3[class='subtitle']")))
                    element_head_text = element_head.text
                    logging.info(f"{element_head_text}")
                except:
                    logging.warning("Shipper not found")

                try:
                    element_head1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[id='shipper'] div[class='box is-fullheight'] div span[itemprop='name']")))
                    element_head_text1 = element_head1.text
                    shipper.append(element_head_text1)
                except:
                    logging.warning("Shipper not found")
                    shipper.append("")

                try:
                    element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[id='shipper'] div[class='box is-fullheight'] div span[itemprop='streetAddress']")))
                    element_text = element.text
                    logging.info(f"{element_text}")
                except:
                    logging.warning("Shipper not found")

                logging.info("-------------------------")
                
                try:
                    element_head = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[id='consignee'] h3[class='subtitle']")))
                    element_head_text = element_head.text
                    logging.info(f"{element_head_text}")
                except:
                    logging.warning("Consignee not found")

                try:
                    element_head1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[id='consignee'] div[class='box is-fullheight'] div span[itemprop='name']")))
                    element_head_text1 = element_head1.text
                    consignee.append(element_head_text1)
                except:
                    logging.warning("consignee not found")
                    consignee.append("")

                try:
                    element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[id='consignee'] div[class='box is-fullheight'] div span[itemprop='streetAddress']")))
                    element_text = element.text
                    logging.info(f"{element_text}")
                except:
                    logging.warning("consignee not found")

                logging.info("-------------------------")
                
                try:
                    element_head = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[id='notify-1'] h3[class='subtitle']")))
                    element_head_text = element_head.text
                    logging.info(f"{element_head_text}")
                except:
                    logging.warning("Notify_party not found")

                try:
                    element_head1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='box is-fullheight'] div b span[itemprop='name']")))
                    element_head_text1 = element_head1.text
                    notify_party.append(element_head_text1)
                except:
                    logging.warning("Notify_party not found")
                    notify_party.append("")

                try:
                    element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[id='notify-1'] div[class='box is-fullheight'] div span[itemprop='streetAddress']")))
                    element_text = element.text
                    logging.info(f"{element_text}")
                except:
                    logging.warning("Notify_party not found")

                logging.info("-------------------------")
                
                try:
                    element_head = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='box'] div[class='column is-4'] h3[class='subtitle']")))
                    element_head_text = element_head.text
                    logging.info(f"{element_head_text}")
                except:
                    logging.warning("Lading_no not found")

                try:
                    element_head1 = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div[class='box'] div[class='column is-4'] div")))
                    element_head_text1 = element_head1.text
                    lading_no.append(element_head_text1)
                except:
                    logging.warning("Lading_no not found")
                    lading_no.append("")


                logging.info("-------------------------")
                searched_importer.append(company)
                browser.back()
            
        df = pd.DataFrame({'Searched Importer':searched_importer,
                                   'Shipper':shipper, 
                                   'Consignee':consignee, 
                                   'Notify Party':notify_party,
                                   'lading_number':lading_no})
                

    return df

def main():
    
    companies = ['Ford Motor Company', 'Toyota', 'Tesla Motors', 'Mercedes-Benz', 'General Motors']
    get_info(companies).to_csv("Information_table1.csv",index=False)

    
if __name__=="__main__":
    main()