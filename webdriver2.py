# -*- coding: utf-8 -*-
"""
Created on Fri May  1 22:02:40 2020

@author: Sogal
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re
chrome = webdriver.Chrome()
chrome.get('en.eztable.com/search')
time.sleep(3)

for i in range(3):
    chrome.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(1)

soup = BeautifulSoup(chrome.page_source, "html.parser")
print(soup)

i = 0
for each_prod in soup.find_all('span', class_ = "sc-gPzReC gOasMm"):
    productName = each_prod.text
    i = i + 1
    print(str(i) + " : " + str(productName))

 #tw.eztable.com/search   
chrome.quit()