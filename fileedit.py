# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 10:48:01 2020

@author: Sogal
"""

import requests
from bs4 import BeautifulSoup
data = requests.get("https://movies.yahoo.com.tw/movie_thisweek.html")
soup = BeautifulSoup(data.text, 'html.parser')
divs = soup.find_all('div', class_= "release_foto")
for index,ele in enumerate(divs):
    print("=================================================")
    print(ele)
    image = ele.find('img')
    if not image:
        continue
    print(str(index + 1) + ": " + image.get("src"))
    img_url = image.get("src")
    img_data = requests.get(img_url)
    print(img_data.content)
    fileName = str(index) + ".jpg"
    file = open(fileName, "bw")
    file.write(img_data.content)
    file.close
#file = open("yahoo.html", "w", encoding='UTF-8')
#file.write(data.text)
#file.close()