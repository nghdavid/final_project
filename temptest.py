import smtplib
from email.mime.text import MIMEText

gmail_user = 'simonlin890327@gmail.com'
gmail_password = 'pbcproject' # your gmail password

msg = MIMEText('成功配對')
msg['Subject'] = '電影訂票'

msg['From'] = gmail_user
msg['To'] = 'b07703057@g.ntu.edu.tw'

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(gmail_user, gmail_password)
server.send_message(msg)
server.quit()

print('Email sent!')