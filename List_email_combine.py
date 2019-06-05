import gspread
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from oauth2client.service_account import ServiceAccountCredentials


auth_json_path = 'C:\\Users\\User\\Desktop\\MovieTogether.json'
gss_scopes = ['https://spreadsheets.google.com/feeds']
#連線
credentials = ServiceAccountCredentials.from_json_keyfile_name(auth_json_path,gss_scopes)
gss_client = gspread.authorize(credentials)
#開啟 Google Sheet 資料表
spreadsheet_key = '1jew8de4bvuBUaw6Fdd12lUh6qVWF7UGST9oZevefhNk' 
sheet = gss_client.open_by_key(spreadsheet_key).sheet1
# Google Sheet 資料表
newMovie = input().split(',')
sheetValue = sheet.get_all_values()
matchPartner = []
match = 0
for i in range(1, len(sheetValue)):
    if i == len(sheetValue) - 1:
        sheet.append_row(newMovie)
    if newMovie[1] == sheetValue[i][1] and newMovie[2] == sheetValue[i][2]:
        matchPartner.append(newMovie)
        matchPartner.append(sheetValue[i])
        sheet.delete_row(i + 1)
        match = 1
        break
    else:
        continue
    
print(matchPartner)

if match == 1:

	chromedriver = 'C:\\Users\\user\\Desktop\\chromedriver'
	driver = webdriver.Chrome(executable_path=chromedriver)
	driver.get('https://mail.google.com/mail/?tab=rm&ogbl')
	q = driver.find_element_by_name('identifier')
	q.send_keys('simonlin890327')
	q.send_keys(Keys.RETURN)
	driver.implicitly_wait(1)
	a = driver.find_element_by_name('password')
	a.send_keys('pbcproject')
	a.send_keys(Keys.RETURN)
	driver.implicitly_wait(1)
	
	b = driver.find_element_by_xpath("//*[@class='T-I J-J5-Ji T-I-KE L3']")
	b.click()
	c = driver.find_element_by_xpath("//*[@class='vO']")
	c.send_keys(matchPartner[0][0])
	driver.implicitly_wait(1)
	d = driver.find_element_by_xpath("//*[@class='aoT']")
	d.send_keys('配對成功')
	driver.implicitly_wait(1)
	e = driver.find_element_by_xpath("//*[@class='Am Al editable LW-avf']")
	e.send_keys('恭喜您配對成功，您的電影為' + matchPartner[0][1] + '，時間為' + matchPartner[0][2] + '，地區為' + matchPartner[0][3] + '。')
	driver.implicitly_wait(1)
	f = driver.find_element_by_xpath("//*[@class='T-I J-J5-Ji aoO v7 T-I-atl L3']")
	f.click()
	time.sleep(5)
	
	b = driver.find_element_by_xpath("//*[@class='T-I J-J5-Ji T-I-KE L3']")
	b.click()
	c = driver.find_element_by_xpath("//*[@class='vO']")
	c.send_keys(matchPartner[1][0])
	driver.implicitly_wait(1)
	d = driver.find_element_by_xpath("//*[@class='aoT']")
	d.send_keys('配對成功')
	driver.implicitly_wait(1)
	e = driver.find_element_by_xpath("//*[@class='Am Al editable LW-avf']")
	e.send_keys('恭喜您配對成功，您的電影為' + matchPartner[1][1] + '，時間為' + matchPartner[1][2] + '，地區為' + matchPartner[1][3] + '。')
	driver.implicitly_wait(1)
	f = driver.find_element_by_xpath("//*[@class='T-I J-J5-Ji aoO v7 T-I-atl L3']")
	f.click()

	time.sleep(5)
	driver.close()