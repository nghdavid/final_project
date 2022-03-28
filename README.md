# 商管程式設計 final project
此專案為我大四修的商管程式設計的final project。總共有5個人參與此project。  
此專案主要的功能是媒合想一起看電影的人，如果想看的場次與電影院都與別人相同的話，那麼配對成功的人們就會收到配對成功的信件。  
使用流程:  
1. 使用者會先填寫google表單來填寫他想看的電影與可以的時間，結果會存在google sheet  
2. 我們會先在yahoo電影把全台灣的電影場次與種類透過爬蟲抓下來  
3. 把資料從yahoo電影網站抓下來後，將資料與google sheet的資料比對。  
4. 最後配對成功的人會收到信件通知  
  
我在這個專案負責的是爬蟲的部分，也就是download.py。 
在dowload.py，我使用bs4套件的BeautifulSoup與requests_html去抓取yahoo電影網站的資料 
在這份code裡，我可以抓取電影的名稱、簡介、上映日期與時刻表。並將資料以dictionary存下來。  



