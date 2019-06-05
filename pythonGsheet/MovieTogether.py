import gspread
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
listdata=input().split(',')
# for i in range(9):
sheet.append_row(listdata)  # 資料內容
sheetValue = sheet.get_all_values()
matchPartner = []
for i in range(1, len(sheetValue)):
    if matchPartner == []:
        matchPartner.append(sheetValue[i])
    else:
        for j in range(len(matchPartner)):
            if sheetValue[i][2] == matchPartner[j][2] and sheetValue[i][1] == matchPartner[j][1]:
                matchPartner.append(sheetValue[i])

print(matchPartner)
# for i in range(len(sheetValue)):
#     if len(sheetValue) == 1:
#         break
#     print(sheetValue[1][0])
#     print(sheetValue)
#     sheetValue.pop(1)
        
        # sheetValue.pop(i)