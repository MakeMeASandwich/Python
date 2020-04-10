# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 10:45:57 2020

@author: Sogal
"""
import re
from bs4 import BeautifulSoup
import requests

data = requests.get("http://www.books.com.tw/web/sys_saletopb/books/02?attribute=30&loc=act_menu_th_46_002")
soup = BeautifulSoup(data.text, "html.parser")
print(soup.prettify()) 

l = 1
print(soup.find("div", class_="type02_bd-a"))
div_items = soup.find_all("div", class_="type02_bd-a")

#for i in div_items:
for index,i in enumerate(div_items):
    print("=====================================================")
    #print(i)
    
    h4 = i.find('h4')
    if not h4:
        continue
    ul = i.find('a')
    print(ul)
    string = str(ul)
    fileName = str(index) + ".txt"
    file = open(fileName, "w+")
    file.write(str(ul))
    file.close
    '''
    if re.match("([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?", string) != None:
        print("success")
    '''
    l = l + 1
    if l > 10:
        break
    


 