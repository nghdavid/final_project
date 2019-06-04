import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

data = input()


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
c.send_keys(data)

d = driver.find_element_by_xpath("//*[@class='aoT']")
d.send_keys('配對成功')

e = driver.find_element_by_xpath("//*[@class='Am Al editable LW-avf']")
e.send_keys('恭喜您配對成功')

f = driver.find_element_by_xpath("//*[@class='T-I J-J5-Ji aoO v7 T-I-atl L3']")
f.click()

time.sleep(5)
driver.close()