#This is the start of a gui function that will be used to test the web scraping
#I ran out of time to finish this so it is not complete

import requests 
import json
import os
import threading
import web_scrap_img
from fake_useragent import UserAgent
from bs4 import BeautifulSoup 

r = requests.get("TestLink", headers={'user-agent':UserAgent().random})
soup = BeautifulSoup(r.content, 'html.parser')

chap_num = soup.find_all(attrs={'data-num':True})

value = []
for num in chap_num:
        value.append(num['data-num'])

target_directory = "FilePath"
filename = "TestName"
full_path = f"{target_directory}/{filename}"


with open(full_path, 'r') as json_file:
        loaded_info =  json.load(json_file)

if loaded_info[0] == value[0]:
        exit()

