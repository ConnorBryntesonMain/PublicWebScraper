import requests 
import json
import os
import re
import web_scrap_img
from fake_useragent import UserAgent
from bs4 import BeautifulSoup 


def chap_list(chapters, count):
    chap = chapters

    r = requests.get(chap, headers={'user-agent':UserAgent().random})
    soup = BeautifulSoup(r.content, 'html.parser')
    chap_num = soup.find_all(attrs={'data-num':True})
    
    chapters = [x.contents[1].attrs['href'] for x in soup.find_all('div', attrs={'class':'eph-num'})]
    name = soup.find('h1', attrs={'class':'entry-title'})
    title = repr(name.text.strip())


    value = []
    for num in chap_num:
        value.append(num['data-num'])
    
    target_directory = "Manhwa"
    temp = str(count) + " " + remove_non_standard_characters(title)
    filename = temp + ".json"
    full_path = f"{target_directory}/{filename}"

    manhwa_full_path = f"{target_directory}/{'manhwa_list.json'}"

    if not os.path.exists(manhwa_full_path) or os.path.getsize(manhwa_full_path) == 0:
        data = []
    else:
        with open (manhwa_full_path, 'r') as json_file:
            data = json.load(json_file)
    info =  str(count) + " " + remove_non_standard_characters(title)
    data.append(info)
    count = 0
    with open (manhwa_full_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    
    data.clear()
    

    if not os.path.exists(full_path) or os.path.getsize(full_path) == 0:
        loaded_info = []
    else:
        with open (full_path, 'r') as json_file:
            loaded_info = json.load(json_file)

    if len(loaded_info) == 0:
        for chapter in chapters:
            print_to_json(temp, web_scrap_img.imgs(chapter), value[count], count)
            count +=1
    elif  loaded_info[0] == value[0]:
        return
    else:
        loaded_info.clear()
        with open (full_path, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        for chapter in chapters:
            print_to_json(temp, web_scrap_img.imgs(chapter), value[count], count)
            count +=1

def print_to_json(name, info, num, count):
    target_directory = "Manhwa"
    filename = name + ".json"
    full_path = f"{target_directory}/{filename}"
    
    
    if not os.path.exists(full_path) or os.path.getsize(full_path) == 0:
        data = []
    else:
        with open (full_path, 'r') as json_file:
            data = json.load(json_file)
    
    data.append(num)
    data.append(info)
    
    with open (full_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)

def remove_non_standard_characters(input_string):
    # Use regular expression to remove non-alphanumeric characters
    clean_string = re.sub(r'[^a-zA-Z0-9]', '', input_string)
    return clean_string