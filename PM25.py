# -*- coding: utf-8 -*-
"""
Created on Fri May 15 18:08:14 2020

@author: Sogal
"""
import requests
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome import Options
from bs4 import BeautifulSoup
from selenium import webdriver

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome = webdriver.Chrome(options=chrome_options)

chrome.get("https://airtw.epa.gov.tw/")
time.sleep(3)

selectCounty = Select(chrome.find_element_by_id('ddl_county'))
selectCounty.select_by_index(1)
time.sleep(1)
selectSite = Select(chrome.find_element_by_id('ddl_site'))
selectSite.select_by_index(4)
time.sleep(4)

soup = BeautifulSoup(chrome.page_source, "html.parser")
air_info = soup.find_all('div', class_= 'info')[0]
state = air_info.find('h4').text[:6]
date = air_info.find('div', class_= 'date').text.strip()[:16]
PM25 = int(air_info.find('span', id = 'PM25').text)
if PM25<16:
    air_quality = "Good" + " PM2.5 - " + str(PM25)
elif PM25<35:
    air_quality = "Moderate" + " PM2.5 - " + str(PM25)
else:
    air_quality = "Unhealthy" + " PM2.5 - " + str(PM25)
    
webhook_key = "Insert Webhook Key"
trigger_name = "Insert Trigger Name"
URL = 'https://maker.ifttt.com/trigger/' + trigger_name + webhook_key + '?value1-()&value2-()&value3-()'.format(date, state, air_quality)
print(date, state, air_quality)