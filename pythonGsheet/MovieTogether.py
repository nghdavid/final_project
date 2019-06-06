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
newMovie = input().split(',')
sheetValue = sheet.get_all_values()
matchPartner = []
for i in range(1, len(sheetValue)):
    if i == len(sheetValue) - 1:
        sheet.append_row(newMovie)
    if newMovie[1] == sheetValue[i][1] and newMovie[2] == sheetValue[i][2]:
        matchPartner.append(newMovie)
        matchPartner.append(sheetValue[i])
        sheet.delete_row(i + 1)
        break
    else:
        continue
    
print(matchPartner)