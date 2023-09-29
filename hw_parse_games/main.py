import json
from time import sleep

import requests
from bs4 import BeautifulSoup

cookies = {
    'PHPSESSID': 'p7vn1m5umokhjm5tvuoabd6e1o',
    '51a55dae53577255b792d39bfe1d40ac': '1',
    '_ga_BB3QC8QLF4': 'GS1.1.1695988914.1.0.1695988914.0.0.0',
    '_ga': 'GA1.1.1912579885.1695988915',
    '_ym_uid': '169598891512312460',
    '_ym_d': '1695988915',
    '_ym_isad': '2',
}

headers = {
    'authority': 'zaka-zaka.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'cache-control': 'no-cache',
    # 'cookie': 'PHPSESSID=p7vn1m5umokhjm5tvuoabd6e1o; 51a55dae53577255b792d39bfe1d40ac=1; _ga_BB3QC8QLF4=GS1.1.1695988914.1.0.1695988914.0.0.0; _ga=GA1.1.1912579885.1695988915; _ym_uid=169598891512312460; _ym_d=1695988915; _ym_isad=2',
    'pragma': 'no-cache',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36',
}

games = {}

for i in range(1, 16):
    print('страница №{}'.format(i))
    response = requests.get(
        'https://zaka-zaka.com/game/new/page{}'.format(i), cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    blocks = soup.find_all('a', class_='game-block')
    for block in blocks:
        if 'game-block-more' in block.get('class'):
            continue
        name = block.find('div', class_='game-block-name').text
        price = block.find('div', class_='game-block-price').text[:-2]
        games[name] = price
    sleep(0.7)

with open('games.json', 'w') as file:
    json.dump(games, file, indent=4)
