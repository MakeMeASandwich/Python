# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 11:32:45 2020

@author: Sogal
"""
import requests
from bs4 import BeautifulSoup
startStation = str(input('Start Station: '))
endStation = str(input('End Station: ')) 
theDay = str(input('Date: '))
timeSelect = str(input('Time: '))
#977abb69-413a-4ccf-a109-0272c24fd490
#9c5ac6ca-ec89-48f8-aab0-41b738cb1814
#2020/04/25
#12:30
postData = {'startStation' : startStation,
            'endStation' : endStation,
            'theDay' : theDay,
            'timeSelect' : timeSelect,
            'waySelect' : 'DepartureInMandarin'}

res = requests.post('https://m.thsrc.com.tw/tw/TimeTable/SearchResultList', postData)

print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')

carNumberList = soup.find_all('div', 'ui-block-a')
carTimeList = soup.find_all('div', 'ui-block-b')
carFreeList = soup.find_all('div', 'ui-block-c')

for i in range(len(carNumberList)):
    print(str(carNumberList[i].text) + 
          ',' + str(carTimeList[i].text) + 
          ',' + str(carFreeList[i].text))