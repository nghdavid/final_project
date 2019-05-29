from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

typelist = []
#chrome_options = Options()  
#chrome_options.add_argument("--headless")
chromedriver = 'C:\\Users\\user\\Desktop\\chromedriver'
driver = webdriver.Chrome(chromedriver)
driver.get('http:google.com')
q = driver.find_element_by_name('q')
q.send_keys('阿凡達 Yahoo電影')
q.send_keys(Keys.RETURN)
a = driver.find_element_by_css_selector('#rso a:nth-child(1)')
a.click()
soup = BeautifulSoup(driver.page_source)
for i in soup.findAll('div', {'class':'level_name'}):
    typem = i.get_text()
    typem = typem.strip()
    for j in range(len(typem)):
        if typem[j] in '期待度滿意度':
            pass
        else:
            typelist.append(typem[j])
    for j in range(len(typelist)):
        print(typelist[j], end = '')
        pass
    pass

print()
print()

for i in soup.findAll('div', {'class':'gray_infobox_inner'}):
    brief = i.get_text()
    print('簡介:' + brief.strip())
print()