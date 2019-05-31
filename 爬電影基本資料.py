# import libs
import requests
import pandas as pd
from bs4 import BeautifulSoup
# 指定所要爬網的URL
url = 'https://movies.yahoo.com.tw/movie_thisweek.html'
# GET request from url and parse via BeautifulSoup
r = requests.get(url)
# 擷取request回傳的文字部分
web_content = r.text
# print(web_content)
r.encoding = 'utf-8' # encoded with format utf-8 for chinese character
# 使用BeautifulSoup來parse HTMl
soup = BeautifulSoup(web_content, 'lxml')
# parse colname 
newMovie2 = soup.find_all('div', class_ = "release_movie_name")
NameCHs = [t.find('a', class_='gabtn').text.replace('\n','').replace(' ','') for t in newMovie2]
NameENs = [t.find('div', class_='en').find('a').text.replace('\n','').replace(' ','') for t in newMovie2]

newMovie3 = soup.find_all('div',class_="release_btn color_btnbox")
Trailers = [t.find('a', class_='btn_s_vedio gabtn')['href'] for t in newMovie3]

newMovie4 = soup.find_all('div',class_="release_text")
Intros = [t.find('span').text.replace('\n','').replace('\r','').replace('\xa0','').replace(' ','') for t in newMovie4]


df = pd.DataFrame(
{
    'Name':NameCHs,
    'EnName':NameENs,
    'Intro': Intros,
    'Trailer': Trailers
})
    
df