import requests 
import json
import os
import web_scap_chaplist
from fake_useragent import UserAgent
from bs4 import BeautifulSoup 

pull = "LINK TO MANHWA"

r = requests.get(pull, headers={'user-agent':UserAgent().random})
soup = BeautifulSoup(r.content, 'html.parser')
temp = soup.findAll('a', {'class': 'series'})
chapters_clean = []

target_directory = "Manhwa"
manhwa_full_path = f"{target_directory}/{'manhwa_list.json'}"

if not os.path.exists(manhwa_full_path) or os.path.getsize(manhwa_full_path) == 0:
    loaded_info = []
    with open(manhwa_full_path, 'w') as json_file:
        json.dump(loaded_info, json_file)
else:
    with open (manhwa_full_path, 'r') as json_file:
        data = json.load(json_file)

with open(manhwa_full_path, 'r') as json_file:
    loaded_info =  json.load(json_file)

loaded_info.clear()

with open(manhwa_full_path, 'w') as json_file:
    json.dump(loaded_info, json_file)

for Sub in temp:
    chapters_clean.append(Sub.attrs['href'])
count = 1
for chap in chapters_clean:
    web_scap_chaplist.chap_list(chap, count)
    count += 1

