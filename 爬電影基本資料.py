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

# create function
def yahooMovieParser(url):
    r = requests.get(url)
    web_content = r.text
    soup = BeautifulSoup(web_content,'lxml')
    newMovie3 = soup.find_all('div',class_="release_btn color_btnbox")
    ###########################
    links = []
    for t in newMovie3:
        try:
            links.append(t.find('a',class_="btn_s_time gabtn")['href'])
        except:
            links.append(0)
    ###########################
    # 中英文片名
    newMovie2 = soup.find_all('div', class_ = "release_movie_name")
    NameCHs = [t.find('a', class_='gabtn').text.replace('\n','').replace(' ','') for t in newMovie2]
    NameENs = [t.find('div', class_='en').find('a').text.replace('\n','').replace(' ','') for t in newMovie2]
    # 預告片
    
    # 電影介紹
    newMovie4 = soup.find_all('div',class_="release_text")
    Intros = [t.find('span').text.replace('\n','').replace('\r','').replace('\xa0','').replace(' ','') for t in newMovie4]
    #合併成data frame
    df = pd.DataFrame(
    {
        'Name':NameCHs,
        'EnName':NameENs,
        'Intro': Intros,
        'time': links
    })
    return df
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

def get_schedule(html):
    schedule = {}
    for i in html.find('div.area_timebox'):
        city = i.text[0:2]
        theater_schedule = {}
        for theater in i.find('ul'):
            
            times = []
            t = theater.text
            t = t.split(' ')
            for x in range(len(t)):
                if x >0:
                    times.append(t[x][-5:-1]+t[x][-1])
            theater_schedule[t[0]] = times       
        
        schedule[city] = theater_schedule
    return schedule
        
url = 'http://movies.yahoo.com.tw/movie_intheaters.html'
urlList = []
 
#while url:
urlList.append(url)
    #url = getNext(url)

    
MovieInfo = None
 
for url in urlList:
    d1 = yahooMovieParser(url)
    if MovieInfo is None:
        MovieInfo = d1
    else:
        MovieInfo = MovieInfo.append(d1,ignore_index=True)
 
for u in urlList:
    d1 = yahooMovieParser(u)
    if MovieInfo is None:
        MovieInfo = d1
    else:
        MovieInfo = MovieInfo.append(d1,ignore_index=True)

schedules = []
for time_url in MovieInfo['time']:
    if time_url == 0:
        schedule = 0
        continue
    session = HTMLSession()
    r = session.get(time_url)
    r.html.render()
    schedules.append(get_schedule(r.html))
    
MovieInfo['schedule'] = schedules

for i in range(len(MovieInfo)):
    print(MovieInfo['Name'][i])  
    print(MovieInfo['EnName'][i])
    print(MovieInfo['Intro'][i])
    print(MovieInfo['schedule'][i])

        

        



