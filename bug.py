#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 29 18:01:08 2019

@author: nghdavid
"""
import bs4,requests
import csv
import re
url = 'https://movies.yahoo.com.tw/movie_intheaters.html'
html = requests.get(url)
html.encoding = 'utf-8'
html.raise_for_status()
objSoup = bs4.BeautifulSoup(html.text,'lxml')
movie = objSoup.find_all("div",class_='release_movie_name')
x = len(movie)

movie_link = objSoup.find_all("a",{"href":re.compile("https://movies.yahoo.com.tw/video")})
movie_time = objSoup.find_all("a",{"href":re.compile("https://movies.yahoo.com.tw/movietime_result.html")})
print(movie_time)
print(movie_time.find("td"))