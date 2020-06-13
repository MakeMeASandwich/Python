# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 10:31:15 2020

@author: Sogal
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import requests

i = 0
chrome = webdriver.Chrome()
chrome.get('https://www.dcard.tw/f/funny')
time.sleep(3)

for i in range(10):
    chrome.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(3)
i = 1
image = chrome.find_elements_by_class_name('t5f2fb-0.McoWn.sc-1v1d5rx-8.cClYde') 
imgurl = image[0].get_attribute('src')

for element in chrome.find_elements_by_class_name('t5f2fb-0.McoWn.sc-1v1d5rx-8.cClYde'):
    imgurl = element.get_attribute('src')
    imgRespond = requests.get(imgurl)
    print(i)
    i = i + 1
    
    file = open(str(i) + ".jpg", "bw")
    file.write(imgRespond.content)
    file.close()
    
    if i > 10:
        break

time.sleep(5)
chrome.quit()
    