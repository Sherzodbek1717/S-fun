import requests
from bs4 import BeautifulSoup
# req = requests.get('https://www.moscowtimes.ru/')
#
# html = req.text
#
# soup = BeautifulSoup(html, 'html.parser')
# col = soup.find('div', class_='col-12')
#
# title = col.find('h3', class_='article-excerpt-lead__headline').get_text(strip= True)
# img = col.find('img')['data-src']
# link = col.find('a')['href']
#
# json_data = [
#     {
#         'title': title,
#         'img': img,
#         'link': link
#     }
# ]
# import json
# with open('statistics.json', mode= 'w', encoding='utf8') as json_file:
#     json.dump(json_data, json_file, indent=4, ensure_ascii=False)




import requests
from bs4 import BeautifulSoup
import json
url = 'https://www.moscowtimes.ru/'
page = 'society'

req = requests.get(url+page)
html = req.text

soup=BeautifulSoup(html, 'html.parser')
blocks = soup.find_all('div', class_='col-4-sm')
json_data = []
for block in blocks:
    title = block.find('p', class_='article-excerpt-default__headline' ).get_text(strip=True)
    image = block.find('img')['data-src']
    link = block.find('a')['href']

    json_data.append(
        {
            'title': title,
            'image': image,
            'link': link
        }
    )

with open('society.json', mode='w', encoding='utf-8') as json_file:
    json.dump(json_data, json_file, indent=4, ensure_ascii=False)

