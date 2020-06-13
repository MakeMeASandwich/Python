# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 09:40:25 2020

@author: Sogal
"""

from bs4 import BeautifulSoup
import requests
import json

#start of code
l = 1
k = 1
j = 1
data = requests.get("http://www.books.com.tw/web/sys_saletopb/books/02?attribute=30&loc=act_menu_th_46_002")
soup = BeautifulSoup(data.text, "html.parser")
print(soup.prettify())
print(soup.find("div", class_="type02_bd-a"))
div_items = soup.find_all("div", class_="type02_bd-a")
jsondict = {}

#for i in div_items:
for index,i in enumerate(div_items):
    print("=====================================================")
    #print(i)
    
    h4 = i.find('h4')
    if not h4:
        continue
    print(str(index+1) + '. ' + h4.text)
    ul = i.find('ul', class_= 'msg')
    li_author = ul.find('li')
    print(li_author.text)  
    author = li_author.text
    l = l + 1
    jsondict.update( {'author' + str(l) : str(author)} )
    li_price = i.find('li', class_='price_a')
    print(li_price.text)
    jsondict.update( {'price' + str(l) : str(li_price.text)} )
    li_name = i.find('a')
    print(li_name)
    jsondict.update( {'title' + str(l) : str(li_name.text)} )
    if l > 10:
        break
print(str(jsondict))
JsonData = json.dumps(jsondict)    
with open("test.json", "w") as file:
    json.dump(jsondict, file)
with open("test.json", "r") as file:
    jsonRead = json.load(file)