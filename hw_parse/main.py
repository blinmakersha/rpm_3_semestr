import json

import requests

cookies = {
    'i': '5MCYdTUIynyRnFcv9IZ701Lfy563nTt2IIbQVqJjOxfgZ6yitMgOk4fbJVRYt2gvgHp/Ki6VcaGwc3jW39wJSgk2MAs=',
    'yandexuid': '9489816011679130661',
    'yuidss': '9489816011679130661',
    'ymex': '1994490661.yrts.1679130661#1994490661.yrtsi.1679130661',
    '_ym_uid': '168096898370128621',
    '_ym_d': '1680968983',
    'skid': '4618210841681104802',
    'gdpr': '0',
    'L': 'CVp7UX5nY15MCHZvbENWdlJ9Q3ZPdWtDPg0JG11DVRc=.1686142098.15366.332800.99cc2e969e9cd558fcfb012b55f2373b',
    'yandex_login': 'valun41c',
    '_ga': 'GA1.2.1865110748.1689418750',
    'is_gdpr': '0',
    'is_gdpr_b': 'CO3+UxCGxAEoAg==',
    'yp': '2001502098.udn.czo2NTE3ODAxMzp2azp2YWx1bjQxaw%3D%3D#1693053417.ygu.1',
    'ys': 'udn.czo2NTE3ODAxMzp2azp2YWx1bjQxaw%3D%3D#c_chck.3470428705',
    'device_id': 'a45dfaf7813fc47fae6a56f138b49f3c5dda6a6f5',
    'chromecast': "''",
    'lastVisitedPage': '%7B%7D',
    'active-browser-timestamp': '1694699246110',
    'Session_id': '3:1695191868.5.0.1686142098156:cdmoyEmm5jSb_wlkANADKg:c4.1.2:1|361080389.0.2.3:1686142098|3:10276017.222385.MZQXjI0uFjmmws6T85l9NKUG9_Q',
    'sessar': '1.1182.CiC-LTkmvlb1ljB-el8XYv0YXJ2NwwuClpn181uNHvoh0w.ElehQFOfRkwdciZ76u1ONVyeH3mIu_E1hBuc04CiABc',
    'sessionid2': '3:1695191868.5.0.1686142098156:cdmoyEmm5jSb_wlkANADKg:c4.1.2:1|361080389.0.2.3:1686142098|3:10276017.222385.fakesign0000000000000000000',
    '_ym_isad': '2',
    '_yasc': 'DZVC44ChVnEcQN0TQe/qSwV7zevovN73bGPVvy4/ZdY8NH2w8XVj3HmHjtbBZnBfJKRbhg==',
    'bh': 'EkAiR29vZ2xlIENocm9tZSI7dj0iMTE3IiwgIk5vdDtBPUJyYW5kIjt2PSI4IiwgIkNocm9taXVtIjt2PSIxMTciGgUiYXJtIiIPIjExNy4wLjU5MzguNjIiKgI/MDIJIk5leHVzIDUiOgcibWFjT1MiQggiMTMuMi4xIkoEIjY0IlJZIkdvb2dsZSBDaHJvbWUiO3Y9IjExNy4wLjU5MzguNjIiLCJOb3Q7QT1CcmFuZCI7dj0iOC4wLjAuMCIsIkNocm9taXVtIjt2PSIxMTcuMC41OTM4LjYyIiI=',
}

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'Accept-Language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # 'Cookie': "i=5MCYdTUIynyRnFcv9IZ701Lfy563nTt2IIbQVqJjOxfgZ6yitMgOk4fbJVRYt2gvgHp/Ki6VcaGwc3jW39wJSgk2MAs=; yandexuid=9489816011679130661; yuidss=9489816011679130661; ymex=1994490661.yrts.1679130661#1994490661.yrtsi.1679130661; _ym_uid=168096898370128621; _ym_d=1680968983; skid=4618210841681104802; gdpr=0; L=CVp7UX5nY15MCHZvbENWdlJ9Q3ZPdWtDPg0JG11DVRc=.1686142098.15366.332800.99cc2e969e9cd558fcfb012b55f2373b; yandex_login=valun41c; _ga=GA1.2.1865110748.1689418750; is_gdpr=0; is_gdpr_b=CO3+UxCGxAEoAg==; yp=2001502098.udn.czo2NTE3ODAxMzp2azp2YWx1bjQxaw%3D%3D#1693053417.ygu.1; ys=udn.czo2NTE3ODAxMzp2azp2YWx1bjQxaw%3D%3D#c_chck.3470428705; device_id=a45dfaf7813fc47fae6a56f138b49f3c5dda6a6f5; chromecast=''; lastVisitedPage=%7B%7D; active-browser-timestamp=1694699246110; Session_id=3:1695191868.5.0.1686142098156:cdmoyEmm5jSb_wlkANADKg:c4.1.2:1|361080389.0.2.3:1686142098|3:10276017.222385.MZQXjI0uFjmmws6T85l9NKUG9_Q; sessar=1.1182.CiC-LTkmvlb1ljB-el8XYv0YXJ2NwwuClpn181uNHvoh0w.ElehQFOfRkwdciZ76u1ONVyeH3mIu_E1hBuc04CiABc; sessionid2=3:1695191868.5.0.1686142098156:cdmoyEmm5jSb_wlkANADKg:c4.1.2:1|361080389.0.2.3:1686142098|3:10276017.222385.fakesign0000000000000000000; _ym_isad=2; _yasc=DZVC44ChVnEcQN0TQe/qSwV7zevovN73bGPVvy4/ZdY8NH2w8XVj3HmHjtbBZnBfJKRbhg==; bh=EkAiR29vZ2xlIENocm9tZSI7dj0iMTE3IiwgIk5vdDtBPUJyYW5kIjt2PSI4IiwgIkNocm9taXVtIjt2PSIxMTciGgUiYXJtIiIPIjExNy4wLjU5MzguNjIiKgI/MDIJIk5leHVzIDUiOgcibWFjT1MiQggiMTMuMi4xIkoEIjY0IlJZIkdvb2dsZSBDaHJvbWUiO3Y9IjExNy4wLjU5MzguNjIiLCJOb3Q7QT1CcmFuZCI7dj0iOC4wLjAuMCIsIkNocm9taXVtIjt2PSIxMTcuMC41OTM4LjYyIiI=",
    'Pragma': 'no-cache',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Mobile Safari/537.36',
    'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
}

params = {
    'what': 'chart',
    'lang': 'ru',
    'external-domain': 'music.yandex.ru',
    'overembed': 'false',
    'ncrnd': '0.4346034032624708',
}

response = requests.get('https://music.yandex.ru/handlers/main.jsx',
                        params=params, cookies=cookies, headers=headers).json()

with open('chart.json', 'w') as f:
    json.dump(response, f, indent=4, ensure_ascii=False)

with open('chart.json', 'r') as f:
    chart = json.load(f)

songs_from_chart = dict()
for ind, about_song in enumerate(chart['chartPositions']):
    song = about_song['track']
    songs_from_chart[ind+1] = {tuple([artist['name']
                                      for artist in song['artists']]): song['title']}

print(songs_from_chart)
