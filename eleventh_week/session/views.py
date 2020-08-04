from django.shortcuts import render, redirect
from .models import Melon_list
import requests
from bs4 import BeautifulSoup

# Create your views here.

def index(request):
    melon_list = Melon_list.objects.all()
    context = {
        'melon_list' : melon_list
    }
    return render(request, 'index.html', context)

def crawling():
    melon_data_list = melon_crawling()
    Melon_list.objects.all().delete()
    for i in range(len(melon_data_list)):
        Melon_list(
            song_name = melon_data_list[i][0],
            artist_name = melon_data_list[i][1],
            rank = int(melon_data_list[i][2]),
            img_src = (melon_data_list[i][3])
        ).save()
        return redirect('index')

def melon_crawling():
    i_am_human = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52'}

    url =  "https://www.melon.com/chart/day/index.htm"

    req = requests.get(url, headers = i_am_human) # 요청할 때 나의 정보도 제시하기 위함(몇몇 사이트에서는 자동으로 크롤링하는 것을 방지하기 위해 이러한 장치를 마련하고 있음 그러므로 내가 사람임을 말해주는 것임)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    song = soup.find_all('div', {"class" : "ellipsis rank01"})
    artist = soup.find_all('div', {"class" : "ellipsis rank02"})
    album = soup.find_all('div', {"class" : "wrap pd_1_12"})
    rank = soup.find_all('span', {"class" : "rank"})
    album_art = soup.select('td:nth-child(4) > div > a > img')

    songs =[]
    for i in song:
        songs.append(i.find('a').text) # text라는걸 찍으면 그것의 text값만 가지고 옴
    artists = []
    for i in artist:
        artists.append(i.find('a').text)
    albums = []
    for i in album:
        albums.append(i.find('a').text)
    ranks = []
    for i in rank[1:]:
        ranks.append(i.text)
    album_arts = []
    for i in album_art:
        album_arts.append(i.get("src"))

    sum_list = list(zip(songs, artists, albums, album_arts)) # zip 함수는 리스트를 합쳐줌
    return(sum_list) # 최종적으로 sum_list를 뱉어냄

