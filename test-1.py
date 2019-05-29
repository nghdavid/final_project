from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

chromedriver = 'C:\\Users\\user\\Desktop\\chromedriver'
driver = webdriver.Chrome(chromedriver)
driver.get('http:google.com')
q = driver.find_element_by_name('q')
q.send_keys('Avengers Yahoo電影')
q.send_keys(Keys.RETURN)
a = driver.find_element_by_css_selector('#rso a:nth-child(1)')
a.click()
soup = BeautifulSoup(driver.page_source)
for i in soup.find('div', {'class':'level_name'}):
    print(i.get_text().strip())
for i in soup.findAll('div', {'class':'gray_infobox_inner'}):
    print(i.get_text().strip())