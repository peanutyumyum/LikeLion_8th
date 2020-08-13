import requests
from bs4 import BeautifulSoup
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Aug0804.settings")
import django
django.setup()
from app.models import melonList
iamhunam = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15'}

url = "https://www.melon.com/chart/day/index.htm"

def melonCrolling():
    req = requests.get(url, headers = iamhunam)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    song = soup.find_all('div', {"class":"ellipsis rank01"})
    songs = []
    for s in song:
        songs.append(s.find('a').text) 
        # s.find('a')의 a 는 a 태그를 의미함

    album = soup.find_all('div', {"class":"ellipsis rank03"})
    albums = []
    for i in album:
        albums.append(i.find('a').text)

    artist = soup.find_all('div', {"class":"ellipsis rank02"})
    artists = []
    for i in artist:
        artists.append(i.find('a').text)

    rank = soup.find_all('span',{"class":"rank"})
    ranks = []
    for j in rank[1:]:
        ranks.append(j.text)

    albumimg = soup.select('td:nth-child(4) > div > a > img')
    imgs = []
    for i in albumimg:
        imgs.append(i.get("src"))
    
    sumlist = list(zip(songs, artists, ranks, imgs))

    return sumlist

if __name__ =='__main__':
    Melon_data_list = melonCrolling()
    melonList.objects.all().delete()
    for i in range(len(Melon_data_list)):
        melonList(
            songName = Melon_data_list[i][0],
            singerName = Melon_data_list[i][1],
            rank = int(Melon_data_list[i][2]),
            imgSrc = Melon_data_list[i][3]
        ).save()