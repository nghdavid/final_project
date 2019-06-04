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
			
    # 電影介紹
    newMovie4 = soup.find_all('div',class_="release_text")
    Intros = [t.find('span').text.replace('\n','').replace('\r','').replace('\xa0','').replace(' ','') for t in newMovie4]
    
    # 中英文片名
    newMovie2 = soup.find_all('div', class_ = "release_movie_name")
    NameCHs = [t.find('a', class_='gabtn').text.replace('\n','').replace(' ','') for t in newMovie2]
    NameENs = [t.find('div', class_='en').find('a').text.replace('\n','').replace(' ','') for t in newMovie2]
    
    #合併成data frame
    df = pd.DataFrame(
    {
        'Name':NameCHs,
        'EnName':NameENs,
		'Intro': Intros,
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

 
Movielist = [] # Movie名稱陣列
 

for i in range(len(MovieInfo)):
	Movielist.append(MovieInfo['Name'][i])  
	

#print(Movielist)



Count = 0
Moviedict = {}	  #電影的dictionary

for j in Movielist:
	Moviedict[j] = []
	Moviedict[j].append(MovieInfo['Name'][Count])       #中文名稱
	Moviedict[j].append(MovieInfo['EnName'][Count])     #英文名稱
	Moviedict[j].append(MovieInfo['Intro'][Count])      #簡介
	Moviedict[j].append(MovieInfo['schedule'][Count])   #時間表

	Count += 1
	for i in range(4):
		print(Moviedict[j][i])   #印出有分行版

#print(Moviedict)     #印出無分行版


