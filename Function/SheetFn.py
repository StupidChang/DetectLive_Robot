import pygsheets
from enum import Enum
import sys
sys.path.append('../../discordrRobot')
from Global import globals
import datetime

# print("get the path------ " + os.getcwd())

if __name__ == "__main__":
    print(sys.path)
    gc = pygsheets.authorize(service_file='../GoogleSheetKey/trusty-fuze-322909-7d29b50ea92c.json')
    sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/180OzY1HVQw1ucU3w5cqJsHSX5LzbVkonYhfTRzelRJo/edit#gid=0')

    print(sheet.worksheets())

    PermissionsSetting = sheet.worksheet_by_title("表情設定")
    MessageID = 1
    Reaction = 3
    RoleID = 5
    # 獲取所有記錄
    rows = PermissionsSetting.get_all_records()

    # 遍歷並刪除符合條件的行
    for row in rows:
        print(row)
        if row['訊息ID'] == MessageID and row['表情'] == Reaction and row['身分組ID'] == RoleID:
            row_number = rows.index(row) + 2  # 轉換為工作表中的行號（從1開始）
            print(row_number)
            PermissionsSetting.delete_rows(row_number)

class LevelEnum(Enum):
    Lv1 = 1
    Lv2 = 50
    Lv3 = 100
    Lv4 = 200
    Lv5 = 300
    Lv6 = 450
    Lv7 = 600
    Lv8 = 750
    Lv9 = 1000
    Lv10 = 1200
    Lv11 = 1400
    Lv12 = 1800
    Lv13 = 2500
    Lv14 = 3750
    Lv15 = 4750
    Lv16 = 5500
    Lv17 = 7000
    Lv18 = 8500
    Lv19 = 10000
    Lv20 = 15000

levelArray = [1, 50, 100, 200, 300, 450 ,600 ,750 ,1000]

# 直播主的資料-------------------------------------------------------------------------------------------------------------
def GetStreamerLiveData():
    gc = pygsheets.authorize(service_file='./GoogleSheetKey/trusty-fuze-322909-7d29b50ea92c.json')
    sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/180OzY1HVQw1ucU3w5cqJsHSX5LzbVkonYhfTRzelRJo/edit#gid=0')

    # print(sheet.worksheets())

    StreamerSetting = sheet.worksheet_by_title("直播設定")
    all_rows_data = StreamerSetting.get_all_values()
    StreamerLiveStatu = [row[:5] for row in all_rows_data[1:] if any(cell.strip() for cell in row)]
    for row in StreamerLiveStatu:
        print(f"[Name = {row[0]}, YTChannelID = {row[1]}, TwitchChannelAddress = {row[2]}, TwitchChannelID = {row[3]}, 身分組 = {row[4]}]")
        value = [row[0], row[1], row[2], row[3], row[4]]
        globals.StreamerLiveStatu.append(value)

async def SetStreamerLiveData(YTname, YTID, TwitchAddress, TwitchID, RoleID):
    gc = pygsheets.authorize(service_file='./GoogleSheetKey/trusty-fuze-322909-7d29b50ea92c.json')
    sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/180OzY1HVQw1ucU3w5cqJsHSX5LzbVkonYhfTRzelRJo/edit#gid=0')

    # print(sheet.worksheets())

    StreamerSetting = sheet.worksheet_by_title("直播設定")
    # Value = [str(YTname), str(YTID), str(TwitchAddress), str(TwitchID), str(RoleID)]
    Value = [YTname, YTID, TwitchAddress, TwitchID, RoleID]
    await StreamerSetting.append_table(values = Value) 
    
# 身分組操作----------------------------------------------------------------------------------------
async def InsertRole(MessageID, Reaction, RoleID):
    gc = pygsheets.authorize(service_file='./GoogleSheetKey/trusty-fuze-322909-7d29b50ea92c.json')
    sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/180OzY1HVQw1ucU3w5cqJsHSX5LzbVkonYhfTRzelRJo/edit#gid=0')

    # print(sheet.worksheets())

    PermissionsSetting = sheet.worksheet_by_title("表情設定")

    values = [MessageID, Reaction, RoleID]# matrix

    for Role in globals.Roles:
        if Role == values:
            return

    await PermissionsSetting.append_table(values = values) 
    GetRole()

def GetRole():
    gc = pygsheets.authorize(service_file='./GoogleSheetKey/trusty-fuze-322909-7d29b50ea92c.json')
    sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/180OzY1HVQw1ucU3w5cqJsHSX5LzbVkonYhfTRzelRJo/edit#gid=0')

    # print(sheet.worksheets())

    PermissionsSetting = sheet.worksheet_by_title("表情設定")
    all_rows_data = PermissionsSetting.get_all_values()
    Permissions_non_empty_rows_data = [row[:3] for row in all_rows_data if any(cell.strip() for cell in row)]
    # print(Permissions_non_empty_rows_data)
    # print(Permissions_non_empty_rows_data[0])
    globals.Roles = []
    for i in range(1, len(Permissions_non_empty_rows_data) ):
        globals.Roles.append(Permissions_non_empty_rows_data[i])
        
    print("表情與身分組:")
    print(globals.Roles)

def DeleteRole(MessageID, Reaction, RoleID):
    gc = pygsheets.authorize(service_file='./GoogleSheetKey/trusty-fuze-322909-7d29b50ea92c.json')
    sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/180OzY1HVQw1ucU3w5cqJsHSX5LzbVkonYhfTRzelRJo/edit#gid=0')

    # print(sheet.worksheets())

    PermissionsSetting = sheet.worksheet_by_title("表情設定")

    # 獲取所有記錄
    rows = PermissionsSetting.get_all_records()

    # 遍歷並刪除符合條件的行
    for row in rows:
        if row['訊息ID'] == MessageID and row['表情'] == Reaction and row['身分組ID'] == RoleID:
            row_number = rows.index(row) + 2  # 轉換為工作表中的行號（從1開始）
            PermissionsSetting.delete_rows(row_number)

# 獲得伺服器的ID-----------------------------------------------------------------------------------------------------------------
def GetServerID():
    gc = pygsheets.authorize(service_file='./GoogleSheetKey/trusty-fuze-322909-7d29b50ea92c.json')
    sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/180OzY1HVQw1ucU3w5cqJsHSX5LzbVkonYhfTRzelRJo/edit#gid=0')

    # print(sheet.worksheets())

    SystemSetting = sheet.worksheet_by_title("系統設定")
    all_rows_data = SystemSetting.get_all_values()

    search_keyword = "伺服器ID:"
    result = None

    # 遍歷資料列，尋找符合搜尋關鍵字的欄位
    for row in all_rows_data:
        if row[0] == search_keyword:
            result = row[1]  # 取得對應的值
            break

    if result is not None:
        print("ServerID搜尋結果：", result)
        globals.ServerID = result
    # else:
    #     print("找不到符合的搜尋結果")

# 獲得Tag頻道ID----------------------------------------------------------------------------------------------------------
def GetTagLiveChannel():
    gc = pygsheets.authorize(service_file='./GoogleSheetKey/trusty-fuze-322909-7d29b50ea92c.json')
    sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/180OzY1HVQw1ucU3w5cqJsHSX5LzbVkonYhfTRzelRJo/edit#gid=0')

    # print(sheet.worksheets())

    SystemSetting = sheet.worksheet_by_title("系統設定")
    all_rows_data = SystemSetting.get_all_values()

    search_keyword = "直播頻道:"
    result = None

    # 遍歷資料列，尋找符合搜尋關鍵字的欄位
    for row in all_rows_data:
        if row[0] == search_keyword:
            result = row[1]  # 取得對應的值
            break

    if result is not None:
        print("LiveChannelID搜尋結果：", result)
        globals.LiveChannelID = result
    # else:
    #     print("找不到符合的搜尋結果")

# 歡迎訊息設定----------------------------------------------------------------------------------------------------------------------
async def SetWelcomeMessage(Message):
    gc = pygsheets.authorize(service_file='./GoogleSheetKey/trusty-fuze-322909-7d29b50ea92c.json')
    sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/180OzY1HVQw1ucU3w5cqJsHSX5LzbVkonYhfTRzelRJo/edit#gid=0')
    Temp = "f\"" + Message + "\""
    print(f"Message = {Message}")

    SystemSetting = sheet.worksheet_by_title("系統設定")
    await SystemSetting.update_value('B1', f"".join(globals.Welcome_Message))

def GetWelcomeMessage():
    gc = pygsheets.authorize(service_file='./GoogleSheetKey/trusty-fuze-322909-7d29b50ea92c.json')
    sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/180OzY1HVQw1ucU3w5cqJsHSX5LzbVkonYhfTRzelRJo/edit#gid=0')

    # print(sheet.worksheets())

    SystemSetting = sheet.worksheet_by_title("系統設定")
    rows = SystemSetting.get_all_values()
            
    for row in rows:
        if(row[0] == "歡迎訊息設定:"):
            globals.Welcome_Message = row[1]


# |||經驗值系統|||
#將Google Sheet的資料抓取製程式內
def GetMemberDataFromSheet():
    gc = pygsheets.authorize(service_file='./GoogleSheetKey/trusty-fuze-322909-7d29b50ea92c.json')
    sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/180OzY1HVQw1ucU3w5cqJsHSX5LzbVkonYhfTRzelRJo/edit#gid=0')

    # print(sheet.worksheets())
    # Setting = sheet.worksheet_by_title("系統設定")
    MemberData = sheet.worksheet_by_title("成員資料")

    # last_column_data = MemberData.get_col(MemberData.cols + 1)[-1] 
    # last_column_data = MemberData.rows 

    all_rows_data = MemberData.get_all_values()
    non_empty_rows_data = [row[:7] for row in all_rows_data if any(cell.strip() for cell in row)]
    print("目前成員資料:")
    # print(non_empty_rows_data)
    for row in non_empty_rows_data:
        if row[0] != "ID":
            globals.DetectLiveMemberData[row[0]] = {
                "Level": int(row[1]),
                "Exp": int(row[2]),
                "Signln": row[3],
                "LevelMessage": row[4],
                "JoinServerDate": row[5],
                "SignInDate": int(row[6])
            }

    print(globals.DetectLiveMemberData)
    
    
    # 非空行的数量
    # non_empty_rows_count = len(non_empty_rows_data)
    # print(non_empty_rows_count)

#執行此程式後，將把執行程式內的MemberData回傳至Google Sheet中
async def SetMemberData2Sheet(): 
    gc = pygsheets.authorize(service_file='./GoogleSheetKey/trusty-fuze-322909-7d29b50ea92c.json')
    sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/180OzY1HVQw1ucU3w5cqJsHSX5LzbVkonYhfTRzelRJo/edit#gid=0')

    MemberData = sheet.worksheet_by_title("成員資料")
    SheetData = MemberData.get_all_values()
    non_empty_rows_data = [row[:1] for row in SheetData if any(cell.strip() for cell in row)]
    print("系統  - 正在執行確認中")
    print(non_empty_rows_data)
    TempData = {}
    
    for row in non_empty_rows_data:
        if row[0] != "ID":
            TempData[row[0]] = {}
    print(TempData)

    data_to_append = []
    for row in globals.DetectLiveMemberData.items():
        if TempData.get(str(row[0])) is None:
            # print(row)
            data_list = [row[0], row[1]["Level"], row[1]["Exp"], row[1]["Signln"], row[1]["LevelMessage"], row[1]["JoinServerDate"], row[1]["SignInDate"]]
            print(data_list)
            data_to_append.append(data_list)
            
    await MemberData.append_table(data_to_append)
    # for row in non_empty_rows_data:
    #     print(non_empty_rows_data)
    #     print(globals.DetectLiveMemberData.get(row[0]))
    #     if row[0] == "ID":
    #         continue
    #     elif( globals.DetectLiveMemberData.get(row[0]) is None):
    #         data_list = [[key] + list(value.values()) for key, value in globals.DetectLiveMemberData.items()]
    #         print(data_list)
    #         # MemberData.append_table(globals.DetectLiveMemberData[i])

async def UpdateMemberData2Sheet(): 
    gc = pygsheets.authorize(service_file='./GoogleSheetKey/trusty-fuze-322909-7d29b50ea92c.json')
    sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/180OzY1HVQw1ucU3w5cqJsHSX5LzbVkonYhfTRzelRJo/edit#gid=0')

    MemberData = sheet.worksheet_by_title("成員資料")
    SheetData = MemberData.get_all_values()
    non_empty_rows_data = [row[:1] for row in SheetData if any(cell.strip() for cell in row)]

    for row_index, row_data in enumerate(non_empty_rows_data):
        for column_index, cell_data in enumerate(row_data):
            if(cell_data == "ID"):
                continue

            print(f"row_index {row_index}")
            print(f"row_data {row_data}")
            print(f"column_index {column_index}")
            print(f"cell_data {cell_data}")
            rownumber = row_index + 1
            range_address = f'A{rownumber}:G{rownumber}'
            data_list = [cell_data, 
                        globals.DetectLiveMemberData[cell_data]["Level"], 
                        str(globals.DetectLiveMemberData[cell_data]["Exp"]), 
                        str(globals.DetectLiveMemberData[cell_data]["Signln"]), 
                        globals.DetectLiveMemberData[cell_data]["LevelMessage"], 
                        globals.DetectLiveMemberData[cell_data]["JoinServerDate"], 
                        str(globals.DetectLiveMemberData[cell_data]["SignInDate"])]
            print(data_list)
            MemberData.update_values(crange=range_address, values=[data_list])
            
    # start_row = 2
    # end_row = 2
    # start_column = 1
    # end_column = 7

    # range_address = f'A{start_row}:G{end_row}'

    # data_list = [row[0], row[1]["Level"], row[1]["Exp"], row[1]["Signln"], row[1]["LevelMessage"], row[1]["JoinServerDate"], row[1]["SignInDate"]]

    # MemberData.update_values(crange=range_address, values=[new_data])
    # for row in non_empty_rows_data:
    #     print(non_empty_rows_data)
    #     print(globals.DetectLiveMemberData.get(row[0]))
    #     if row[0] == "ID":
    #         continue
    #     elif( globals.DetectLiveMemberData.get(row[0]) is None):
    #         data_list = [[key] + list(value.values()) for key, value in globals.DetectLiveMemberData.items()]
    #         print(data_list)
    #         # MemberData.append_table(globals.DetectLiveMemberData[i])

def AddNewMemberDataFromGlobals(ID):
    # print(type(ID))
    # print(type(str(ID)))

    if(globals.DetectLiveMemberData[str(ID)] is None):
        time = datetime.datetime.now()
        formatted_time = time.strftime("%Y/%m/%d/%H")
        # globals.DetectLiveMemberData.append(Value)
        globals.DetectLiveMemberData[str(ID)] = {
                "Level": 1,
                "Exp": 0,
                "Signln": "FALSE",
                "LevelMessage": "None",
                "JoinServerDate": str(formatted_time),
                "SignInDate" : 0
            }
    else:
        print("[系統訊息] - 已有此成員資料")
def AddExp(ID, AddExp):
    globals.DetectLiveMemberData[str(ID)]['Exp'] += AddExp
    


    










