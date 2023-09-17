import requests
from bs4 import BeautifulSoup

url = ''

def downloader_uzmovi(url: str):
    if url.startswith('http://uzmovi.com/') or url.startswith('https://uzmovi.com/'):
        response = requests.get(url=url)
        
        parser_data = BeautifulSoup(response.text, features='html.parser')
        data ={}
        try:
            links = parser_data.find_all(name='a',attrs={'class':'btn1'})
            urls = {}
            for link in links:
                if 'YUKLAB OLISH' in link.text:
                    urls[link.text] = link['href']
                data['urls'] = urls
            return links
        except:
            data['urls'] = {}
        
        try:
            image = parser_data.find(name='div',attrs={'class':'fstory-poster'})
            photo = image.img
            data['photo'] = photo['data-src']
        except:
            data['photo'] = ''
    else:
        return {"status":204 , 'info':"Invalid url"}
    

print(downloader_uzmovi(url="http://uzmovi.com/tarjima-kinolarri/5607-meg-2-premyera-uzbek-ozbek-tilida.html"))