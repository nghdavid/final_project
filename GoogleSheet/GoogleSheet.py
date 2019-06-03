import sys
import time
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC
GDriveJSON = 'C:\\Users\\User\\Desktop\\GoogleSheet\\PythonUpload.json'
GSpreadSheet = '電影配不配'
WaitSecond = 60
print('將資料記錄在試算表' ,GSpreadSheet , '每' ,WaitSecond ,'秒')
print('按下 Ctrl-C中斷執行')
count = 1
while True:
    try:
        scope = ['https://spreadsheets.google.com/feeds']
        key = SAC.from_json_keyfile_name(GDriveJSON, scope)
        gc = gspread.authorize(key)
        worksheet = gc.open(GSpreadSheet).sheet1
    except Exception as ex:
        print('無法連線Google試算表', ex)
        sys.exit(1)
    worksheet.append_row((datetime.datetime.now(), count))
    count = count+1
    print('新增一列資料到試算表' ,GSpreadSheet)
    time.sleep(WaitSecond)


# import json
# import sys
# import time
# import datetime


# import gspread
# from oauth2client.service_account import ServiceAccountCredentials

# GDOCS_OAUTH_JSON = 'C:\\Users\\User\\Desktop\\PythonUpload.json' 
# GDOCS_SPREADSHEET_NAME = "電影配不配"
# FREQUENCY_SECONDS      = 2

# print('將資料記錄在試算表',GDOCS_SPREADSHEET_NAME,'每',1/FREQUENCY_SECONDS,'秒')

# def login_open_sheet(oauth_key_file, spreadsheet):
#     """Connect to Google Docs spreadsheet and return the first worksheet."""
#     try:
#         scope =  ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
#         credentials = ServiceAccountCredentials.from_json_keyfile_name(oauth_key_file, scope)
#         gc = gspread.authorize(credentials)
#         worksheet = gc.open(spreadsheet).sheet1
#         return worksheet
#     except Exception as ex:
#         print('Unable to login and get spreadsheet.  Check OAuth credentials, spreadsheet name, and make sure spreadsheet is shared to the client_email address in the OAuth .json file!')
#         print('Google sheet login failed with error:', ex)
#         sys.exit(1)
        
# print('Logging sensor measurements to {0} every {1} seconds.'.format(GDOCS_SPREADSHEET_NAME, FREQUENCY_SECONDS))
# print('Press Ctrl-C to quit.')
# worksheet = None

# while True:
#     # Login if necessary.
#     if worksheet is None:
#         worksheet = login_open_sheet(GDOCS_OAUTH_JSON, GDOCS_SPREADSHEET_NAME)

#     # Append the data in the spreadsheet, including a timestamp
#     try:
#         worksheet.update_acell('A1','Bingo!') #更新某個儲存格
#         #value = 10
#         #worksheet.append_row((datetime.datetime.now(), value)) #將資料加在最下方
#     except:
#         # Error appending data, most likely because credentials are stale.
#         # Null out the worksheet so a login is performed at the top of the loop.
#         print('Error, logging in again')
#         worksheet = None
#         time.sleep(FREQUENCY_SECONDS)
#         continue

#     # Wait 30 seconds before continuing
#     print('Wrote a row to {0}'.format(GDOCS_SPREADSHEET_NAME))
#     time.sleep(FREQUENCY_SECONDS)
