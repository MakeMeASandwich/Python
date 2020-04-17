# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 11:52:27 2020

@author: Sogal
"""

import requests, json
res = requests.get('https://www.dcard.tw/service/api/v2/forums/pet/posts?popular=true&limit=40&before=233492236')
data = json.loads(res.text)

with open("test.json", "w") as file:
    json.dump(data, file)
with open("test.json", "r") as file:
    jsonRead = json.load(file)

for i in data:
    json.dump('title', file)
    json.dump('gender', file)
    json.dump('school', file)
    json.dump('topics', file)