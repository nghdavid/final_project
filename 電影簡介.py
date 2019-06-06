from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

data = input()
chrome_options = Options() # 啟動無頭模式
chrome_options.add_argument('--headless')  #規避google bug
chrome_options.add_argument('--disable-gpu')

chromedriver = 'C:\\Users\\user\\Desktop\\chromedriver'
driver = webdriver.Chrome(executable_path=chromedriver, chrome_options=chrome_options)
driver.get('http:google.com')
q = driver.find_element_by_name('q')
q.send_keys(data + ' Yahoo電影')
q.send_keys(Keys.RETURN)
a = driver.find_element_by_css_selector('#rso a:nth-child(1)')
a.click()
soup = BeautifulSoup(driver.page_source)
print('類型: ', end = '')
for i in soup.findAll('div', {'class':'level_name_box'}):
    for j in i.findAll('div', {'class':'level_name'}):
        typem = j.get_text()
        typem = typem.strip()
        print(typem, end = ' ')

print()
print()

for i in soup.find('div', {'class':'movie_intro_info_r'}).findAll('span')[0]:
            typem = i
            typem = typem.strip()
            print(typem)
            break
for i in soup.find('div', {'class':'movie_intro_info_r'}).findAll('span')[1]:
            typem = i
            typem = typem.strip()
            print(typem)
            break
for i in soup.find('div', {'class':'movie_intro_info_r'}).findAll('span')[3]:
            typem = i
            typem = typem.strip()
            print(typem)
            break
driver.back()
driver.back()            
print()

print('簡介: ', end = '')
q = driver.find_element_by_name('q')
q.send_keys(data + ' 開眼電影')
q.send_keys(Keys.RETURN)
a = driver.find_element_by_css_selector('#rso a:nth-child(1)')
a.click()
soup = BeautifulSoup(driver.page_source)
for i in soup.find('div', {'id':'filmTagBlock'}).findAll('span')[2]:
    brief = i
    brief = str(brief)
    brief = brief.strip()
    print(brief)
    break
    
print()


driver.close()