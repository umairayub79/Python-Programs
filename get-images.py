import requests
from bs4 import BeautifulSoup as bs
import os
import random

url = 'https://www.pexels.com/search/abstract/'

page = requests.get(url)
soup = bs(page.text, 'html.parser')

image_tags = soup.findAll('img')

if not os.path.exists('imgs'):
    os.makedirs('imgs')
    print("IMAGE DIR CREATED")

os.chdir('imgs')

x = 0
for image in image_tags:
    try:
        url = image['src']
        print(str(url)) 
        if 'photos' in url: 
            source = requests.get(url)
            if source.status_code == 200:
                with open('wall-' + str(x) + '.jpg', 'wb') as f:
                    f.write(requests.get(url).content)
                    f.close()
                    x += 1
                    x += random.randint(1,99) 
                    print("wall- " + str(x))
    except:
        pass
