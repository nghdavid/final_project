#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 00:34:05 2019

@author: nghdavid
"""
import pandas as pd
import requests
from bs4 import BeautifulSoup
from requests_html import HTMLSession


# It takes a yahoo website as input
# It returns a panda dataframe that contains lists of Chinese names and English names and schedule websites  
def yahooMovieParser(url):
    r = requests.get(url)
    web_content = r.text
    soup = BeautifulSoup(web_content,'lxml')
    #時刻表
    newMovie3 = soup.find_all('div',class_="release_btn color_btnbox")
    
    links = []
    for t in newMovie3:
        try:
            links.append(t.find('a',class_="btn_s_time gabtn")['href'])
        except:
            links.append(0)
    
    # 中英文片名
    newMovie2 = soup.find_all('div', class_ = "release_movie_name")
    NameCHs = [t.find('a', class_='gabtn').text.replace('\n','').replace(' ','') for t in newMovie2]
    NameENs = [t.find('div', class_='en').find('a').text.replace('\n','').replace(' ','') for t in newMovie2]
    
    #合併成data frame
    df = pd.DataFrame(
    {
        'Name':NameCHs,
        'EnName':NameENs,
        'time': links
    })
    return df
#A function that take website as input
#It returns next webpage
def getNext(url):
    r = requests.get(url)
    web_content = r.text
    soup = BeautifulSoup(web_content,'lxml')
    pageInfo = soup.find('div', class_='page_numbox')
    tagA = pageInfo.find('li', class_="nexttxt").find('a')
    if tagA:
        return tagA['href']
    else:
        return None
#A function that take schedule website as input
#It returns a dictionary that store time
def get_schedule(html):
    schedule = {}
    for i in html.find('div.area_timebox'):
        city = i.text[0:2]
        theater_schedule = {}#It store theaters in a same city
        for theater in i.find('ul'):
            
            times = []
            t = theater.text
            t = t.split(' ')
            for x in range(len(t)):
                if x >0:
                    times.append(t[x][-5:-1]+t[x][-1])#time as string
            theater_schedule[t[0]] = times#t[0] is theater       
        
        schedule[city] = theater_schedule
    return schedule
<<<<<<< HEAD

#Input 為 電影的主頁
#Output 為 電影種類 imdb分數 上映日期 電影長度 電影圖片網址
#如果查不到 imdb，就回傳 電影種類 -1 上映日期 電影長度 電影圖片網址
def get_type(time_url):
    #進到網頁拿html
    r = requests.get(time_url)
    web_content = r.text
    soup = BeautifulSoup(web_content,'lxml')
    info = soup.find('div', class_='level_name')
    info1 = soup.find_all('span')
    types = info.text.replace('\n','').replace(' ','')
    types = types.split('/')
    photo = soup.find('div', class_='movie_intro_foto').find('img')['src']
    has_imdb = 0#有無imdb
    for i in info1:
        if i.text[0:4] == 'IMDb':
            imdb = float(i.text[7:-1]+i.text[-1])
            has_imdb = 1
        if i.text[0:4] == '上映日期':
            date = i.text[5:-1]+i.text[-1]
        if len(i.text)>0:
            if i.text[0] == '片':
                length = i.text[6:-1]+i.text[-1]
    if has_imdb:
        return types,imdb,date,length,photo
    else:
        return types,-1,date,length,photo
    


=======
        
>>>>>>> parent of 1e91d08... Increase download.py function
url = 'http://movies.yahoo.com.tw/movie_intheaters.html'
urlList = []
 
while url:
    urlList.append(url)
    url = getNext(url)

#Get Chinese names and English names and schedule websites 
MovieInfo = None
for url in urlList:
    d1 = yahooMovieParser(url)
    if MovieInfo is None:
        MovieInfo = d1
    else:
        MovieInfo = MovieInfo.append(d1,ignore_index=True)

#
#Get schedules
schedules = []
for time_url in MovieInfo['time']:
    if time_url == 0:
        schedule = 0
        schedules.append(schedule)
        continue
    session = HTMLSession()
    r = session.get(time_url)
    r.html.render()
    schedules.append(get_schedule(r.html))
MovieInfo['schedule'] = schedules

<<<<<<< HEAD
#爬 電影種類 imdb分數 上映日期 電影長度 電影圖片網址
types = []
imdbs = []
dates = []
lengths = []
photos = []
for time_url in MovieInfo['Web']:
    type,imdb,date,length,photo = get_type(time_url)
    types.append(type)
    ################################
    imdbs.append(imdb)#請注意，如果imdb為-1這代表查不到imdb
    ################################
    dates.append(date)
    lengths.append(length)
    photos.append(photo)
#併到dataframe
MovieInfo['type'] = types
MovieInfo['imdb'] = imdbs
MovieInfo['release_date'] = dates
MovieInfo['length'] = lengths
MovieInfo['photo_website'] = photos#電影圖片網址


for i in range(len(MovieInfo)):
    print(MovieInfo['Name'][i])  
    print(MovieInfo['type'][i])
    print(MovieInfo['imdb'][i])
    print(MovieInfo['release_date'][i])
    print(MovieInfo['length'][i])
    print(MovieInfo['photo_website'][i])
    print()
=======
 

for i in range(len(MovieInfo)):
    print(MovieInfo['Name'][i])  
    print(MovieInfo['EnName'][i])
    print(MovieInfo['schedule'][i])
>>>>>>> parent of 1e91d08... Increase download.py function



