# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 10:21:55 2020

@author: Sogal
"""
from bs4 import BeautifulSoup
import requests
data = """
<html>
<head>
    <title>Phoebe's Fantasy journey</title>
    <link href="style.css" rel=stylesheet>
</head>
<body>
<div>
    <header>
    
    </header>
        <h1>為無奈的工作人生添加一點趣味吧！</h1>
在這裡菲比會分享日常小事，像是上班途中發現的巷弄美食、文青咖啡店<br>
又或是學了什麼新的知識，都會在這邊分享給大家
        <h2>菲比尋常的奇幻旅程</h2>
        <a href="www.yahoo.com" class="L"> Find Something</a><br>
        <a href="www.google.com" class="b"> Find Something</a><br>
</div>

</body>
</html>
"""

data = requests.get("http://www.books.com.tw/web/sys_saletopb/books/02?attribute=30&loc=act_menu_th_46_002")
soup = BeautifulSoup(data.text, "html.parser")
print(soup.prettify())
'''
print("=====================================================")
print(soup.title)
print("=====================================================")
print(soup.a)
print("=====================================================")
print(soup.a.attrs)
print("=====================================================")
print(soup.a.text)
print("=====================================================")
print(soup.find("a"))
print("=====================================================")
print(soup.find_all("a"))
print("=====================================================")
print(soup.find_all("a", href="www.google.com"))
print("=====================================================")
print(soup.find_all("a", class_="b"))
print("=====================================================")
print(soup.find_all("a", href="www.yahoo.com"))
'''
#start of code
l = 0
print(soup.find("div", class_="type02_bd-a"))
div_items = soup.find_all("div", class_="type02_bd-a")

for i in div_items:
    print("=====================================================")
    #print(i)
    
    h4 = i.find('h4')
    print(h4.text)
    ul = i.find('ul', class_= 'msg')
    li_author = ul.find('li')
    print(li_author.text)  
    li_price = i.find('li', class_='price_a')
    print(li_price.text)
    l = l + 1
    if l > 100:
        break