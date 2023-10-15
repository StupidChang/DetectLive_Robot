import pygsheets
import sys
sys.path.append('../../discordrRobot')
from Global import globals
import datetime
from googleapiclient.discovery import build
import discord
import asyncio
from discord.ext import commands
# print("get the path------ " + os.getcwd())

class SheetFunction(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def Function(self, ctx, *args):
        print()

    def Mytest(self):
        print("test2")

    # 直播主的資料-------------------------------------------------------------------------------------------------------------
    def GetStreamerLiveData():
        globals.StreamerLiveStatu = []
        gc = pygsheets.authorize(service_file='./GoogleSheetKey/trusty-fuze-322909-7d29b50ea92c.json')
        sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/180OzY1HVQw1ucU3w5cqJsHSX5LzbVkonYhfTRzelRJo/edit#gid=0')

        # print(sheet.worksheets())

        StreamerSetting = sheet.worksheet_by_title("直播設定")
        all_rows_data = StreamerSetting.get_all_values()
        StreamerLiveStatu = [row[:6] for row in all_rows_data[1:] if any(cell.strip() for cell in row)]
        for row in StreamerLiveStatu:
            print(f"[Name = {row[0]}, YTChannelID = {row[1]}, TwitchChannelAddress = {row[2]}, TwitchChannelID = {row[3]}, 身分組 = {row[4]}, 頻道 = {row[5]}]")
            value = [row[0], row[1], row[2], row[3], row[4], row[5]]
            globals.StreamerLiveStatu.append(value)

    async def SetStreamerLiveData(YTname, YTID, TwitchAddress, TwitchID, RoleID, ctx):
        gc = pygsheets.authorize(service_file='./GoogleSheetKey/trusty-fuze-322909-7d29b50ea92c.json')
        sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/180OzY1HVQw1ucU3w5cqJsHSX5LzbVkonYhfTRzelRJo/edit#gid=0')

        # print(sheet.worksheets())

        StreamerSetting = sheet.worksheet_by_title("直播設定")
        # Value = [str(YTname), str(YTID), str(TwitchAddress), str(TwitchID), str(RoleID)]
        Value = [YTname, YTID, TwitchAddress, TwitchID, RoleID]
        await StreamerSetting.append_table(values = Value) 
        SheetFunction.GetStreamerLiveData()

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
        SheetFunction.GetRole()

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

    def GetExperienceChannel():
        gc = pygsheets.authorize(service_file='./GoogleSheetKey/trusty-fuze-322909-7d29b50ea92c.json')
        sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/180OzY1HVQw1ucU3w5cqJsHSX5LzbVkonYhfTRzelRJo/edit#gid=0')

        SystemSetting = sheet.worksheet_by_title("系統設定")
        all_rows_data = SystemSetting.get_all_values()

        search_keyword = "經驗值頻道:"
        result = None

        # 遍歷資料列，尋找符合搜尋關鍵字的欄位
        for row in all_rows_data:
            if row[0] == search_keyword:
                result = row[1]  # 取得對應的值
                break

        if result is not None:
            result = result.split(', ')
            for row in result:
                # print(result)
                globals.ExperienceChannelID[row] = {}
            print(globals.ExperienceChannelID)
        # else:
        #     print("找不到符合的搜尋結果")

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
        non_empty_rows_data = [row[:13] for row in all_rows_data if any(cell.strip() for cell in row)]
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
                    "SignInDate": int(row[6]),
                    "Activity": row[7],
                    "title" : row[8],
                    "alltitle" : row[9],
                    "image_url" : row[10],
                    "MoraWinNumber" : int(row[11]),
                    "Mission" : row[12]
                }

        print(globals.DetectLiveMemberData)
        
        # 非空行的数量
        # non_empty_rows_count = len(non_empty_rows_data)
        # print(non_empty_rows_count)

    #執行此程式後，將把執行程式內的MemberData回傳至Google Sheet中
    async def CheckMemberData2Sheet(): 
        gc = pygsheets.authorize(service_file='./GoogleSheetKey/trusty-fuze-322909-7d29b50ea92c.json')
        sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/180OzY1HVQw1ucU3w5cqJsHSX5LzbVkonYhfTRzelRJo/edit#gid=0')

        MemberData = sheet.worksheet_by_title("成員資料")
        SheetData = MemberData.get_all_values()
        non_empty_rows_data = [row[:1] for row in SheetData if any(cell.strip() for cell in row)]
        print("[系統訊息] - 正在執行確認是否有新增成員中...")
        print(non_empty_rows_data)
        TempData = {}
        
        for row in non_empty_rows_data:
            if row[0] != "ID":
                TempData[row[0]] = {}
        print(f"TempData = {TempData}")

        data_to_append = []
        for row in globals.DetectLiveMemberData.items():
            if TempData.get(str(row[0])) is None:
                # print(row)
                data_list = [row[0], row[1]["Level"], row[1]["Exp"], row[1]["Signln"], row[1]["LevelMessage"], row[1]["JoinServerDate"], row[1]["SignInDate"], row[1]["Activity"], row[1]["title"], row[1]["alltitle"], row[1]["image_url"], row[1]["MoraWinNumber"], row[1]["Mission"]]
                print(f"data_list = {data_list}")
                data_to_append.append(data_list)
        
        if len(data_to_append) != 0:
            try:
                await MemberData.append_table(data_to_append)
            except:
                print("[備份系統] - 發生錯誤")

        print("[系統訊息] - 結束執行")
        # for row in non_empty_rows_data:
        #     print(non_empty_rows_data)
        #     print(globals.DetectLiveMemberData.get(row[0]))
        #     if row[0] == "ID":
        #         continue
        #     elif( globals.DetectLiveMemberData.get(row[0]) is None):
        #         data_list = [[key] + list(value.values()) for key, value in globals.DetectLiveMemberData.items()]
        #         print(data_list)
        #         # MemberData.append_table(globals.DetectLiveMemberData[i])

    async def SetNewMemberData2Sheet(): 
        gc = pygsheets.authorize(service_file='./GoogleSheetKey/trusty-fuze-322909-7d29b50ea92c.json')
        sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/180OzY1HVQw1ucU3w5cqJsHSX5LzbVkonYhfTRzelRJo/edit#gid=0')

        MemberData = sheet.worksheet_by_title("成員資料")
        SheetData = MemberData.get_all_values()
        non_empty_rows_data = [row[:1] for row in SheetData if any(cell.strip() for cell in row)]
        print("[系統訊息] - 正在執行確認是否有新增成員中...")
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
                data_list = [row[0], row[1]["Level"], row[1]["Exp"], row[1]["Signln"], row[1]["LevelMessage"], row[1]["JoinServerDate"], row[1]["SignInDate"], row[1]["Activity"], row[1]["title"], row[1]["alltitle"], row[1]["image_url"], row[1]["MoraWinNumber"], row[1]["Mission"]]
                print(f"data_list = {data_list}")
                data_to_append.append(data_list)
        
        if len(data_to_append) != 0:
            try:
                await MemberData.append_table(data_to_append)
            except:
                print("[備份系統] - 發生錯誤")

        print("[系統訊息] - 結束執行")
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
        print(f"[備份系統] - 開始更新系統資料於DataBase...")
        for row_index, row_data in enumerate(non_empty_rows_data):
            for column_index, cell_data in enumerate(row_data):
                if(cell_data == "ID"):
                    continue
                
                # print(f"row_index {row_index}")
                # print(f"row_data {row_data}")
                # print(f"column_index {column_index}")
                # print(f"cell_data {cell_data}")
                rownumber = row_index + 1
                range_address = f'A{rownumber}:M{rownumber}'
                data_list = [cell_data, 
                            globals.DetectLiveMemberData[cell_data]["Level"], 
                            str(globals.DetectLiveMemberData[cell_data]["Exp"]), 
                            str(globals.DetectLiveMemberData[cell_data]["Signln"]), 
                            globals.DetectLiveMemberData[cell_data]["LevelMessage"], 
                            globals.DetectLiveMemberData[cell_data]["JoinServerDate"], 
                            str(globals.DetectLiveMemberData[cell_data]["SignInDate"]),
                            globals.DetectLiveMemberData[cell_data]["Activity"],
                            globals.DetectLiveMemberData[cell_data]["title"],
                            globals.DetectLiveMemberData[cell_data]["alltitle"],
                            globals.DetectLiveMemberData[cell_data]["image_url"],
                            globals.DetectLiveMemberData[cell_data]["MoraWinNumber"],
                            globals.DetectLiveMemberData[cell_data]["Mission"]]
                print(data_list)
                # MemberData.update_values(crange=range_address, values=[data_list])
                await asyncio.to_thread(MemberData.update_values, crange=range_address, values=[data_list])  # 使用 asyncio.to_thread 進行非同步操作
                
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

    def AddNewMemberData2Globals(ID):
        # print(type(ID))
        # print(type(str(ID)))

        if str(ID) not in globals.DetectLiveMemberData:
            time = datetime.datetime.now()
            formatted_time = time.strftime("%Y/%m/%d - %H:%M")
            # globals.DetectLiveMemberData.append(Value)
            globals.DetectLiveMemberData[str(ID)] = {
                    "Level": 1,
                    "Exp": 0,
                    "Signln": "FALSE",
                    "LevelMessage": "這位小粉絲尚未新增自我介紹喔~!",
                    "JoinServerDate": str(formatted_time),
                    "SignInDate" : 0,
                    "Activity" : "尚無活動!",
                    "title" : "",
                    "alltitle" : "",
                    "image_url" : "",
                    "MoraWinNumber" : 0,
                    "Mission" : ""
                }
            print("[系統訊息] - 無此成員資料，已新增至系統內")
        else:
            print("[系統訊息] - 已有此成員資料")

    def AddExp(ID, AddExp):
        globals.DetectLiveMemberData[str(ID)]['Exp'] += AddExp

    # 搜尋影片是否有直播
    async def SearchYoutubeStreamStatus(ChannelID, VideoURL, VideoID, ctx):
        try:
            youtube = build('youtube', 'v3', developerKey="AIzaSyBdXrPPQN2BEelDvWsW_h9Rxtwi0eas79I")
            response = youtube.videos().list(
                part='liveStreamingDetails',
                id=VideoID
            ).execute()
            print(f"response = {response}")
            # print(f"live_streams_response = {live_streams_response}")
            if 'items' in response:
                if len(response['items']) > 0:
                    video_info = response['items'][0]
                    if 'liveStreamingDetails' in video_info:
                        if 'actualEndTime' not in video_info['liveStreamingDetails']:
                            if 'actualStartTime' in video_info['liveStreamingDetails']:
                                if VideoID not in globals.VideoStatus:
                                    globals.VideoStatus[VideoID] = {    
                                        # "Name":row[0],
                                        "ChannelID":ChannelID,
                                        "VideoURL":VideoURL,
                                        "StreamStatus":"False"
                                    }   
                                if(globals.VideoStatus[VideoID]['StreamStatus'] != "True"):
                                    for row in globals.StreamerLiveStatu:
                                        if row[1] == ChannelID:
                                            channel = ctx.guild.get_channel(int(row[5]))
                                            globals.VideoStatus[VideoID]['StreamStatus'] = "True"
                                            # Tagchannel = ctx.guild.get_channel(int(globals.LiveChannelID))
                                            TagMessage = (
                                                            f"🔴 {row[0]} 直播中...!\n"
                                                            f"<@&{row[4]}> <@&1065083845487108096> 直播開始了!! 快來看看吧!!\n"
                                                            f"{VideoURL}\n"
                                                        )
                                            await channel.send(TagMessage)
                            else:
                                # print(VideoID)
                                # print(globals.VideoStatus)
                                # print(VideoID not in globals.VideoStatus)
                                if VideoID not in globals.VideoStatus:
                                    globals.VideoStatus[VideoID] = {    
                                        # "Name":row[0],
                                        "ChannelID":ChannelID,
                                        "VideoURL":VideoURL,
                                        "StreamStatus":"False"
                                    }  
                                    for row in globals.StreamerLiveStatu:
                                        channel = ctx.guild.get_channel(int(row[5]))
                                        # Tagchannel = ctx.guild.get_channel(int(globals.LiveChannelID))
                                        # print(row)
                                        # print(row[1] == ChannelID)
                                        if row[1] == ChannelID:
                                            TagMessage = (
                                                            f"🟠 {row[0]} 發布了一個新的直播拉...!\n"
                                                            f"<@&{row[4]}> <@&1065083845487108096> 直播即將開始!! 快進入直播間等待吧!!\n"
                                                            f"{VideoURL}\n"
                                                        )
                                            # await Tagchannel.send(TagMessage)
                                            await channel.send(TagMessage)
                        else:
                            globals.WillBeDelete.append(VideoID)                    
                else:
                    globals.WillBeDelete.append(VideoID)
        except Exception as e:
            print(e)
        

    # ==================================稱號系統=========================================
    def GetTitle():
        try:
            gc = pygsheets.authorize(service_file='./GoogleSheetKey/trusty-fuze-322909-7d29b50ea92c.json')
            sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/180OzY1HVQw1ucU3w5cqJsHSX5LzbVkonYhfTRzelRJo/edit#gid=0')

            TitleData = sheet.worksheet_by_title("稱號資料")
            SheetData = TitleData.get_all_values()
            non_empty_rows_data = [row[:4] for row in SheetData if any(cell.strip() for cell in row)]
            # print(len(non_empty_rows_data))
            for row in non_empty_rows_data:
                print(row)
                if(row[0] != "稱號編號"):
                    globals.DetectLiveTitleData[row[0]] = {
                        'label':row[1],
                        'emoji':row[2],
                        'description':row[3]
                    }
            print(globals.DetectLiveTitleData)
        except Exception as e:
            print(e)


    async def SendTitle(titleNumber, LimitTime, ctx):
        isLimit = False
        view = discord.ui.View()
        button = discord.ui.Button(
            emoji="📩",
            label="領取稱號",
            style=discord.ButtonStyle.green,
            disabled=isLimit
        )

        async def CB(interaction: discord.Interaction):
            await interaction.response.defer()
            if isLimit:
                button.disabled = isLimit
                await interaction.message.edit(view=view)
            else:
                print(interaction.user.id)
                if interaction.user.id not in globals.SetNewMemberTitle:
                    try:
                        await ctx.send(f"{interaction.user} 已領取了稱號 **>>>> {globals.DetectLiveTitleData[str(titleNumber)]['emoji']} {globals.DetectLiveTitleData[str(titleNumber)]['label']} <<<<**")
                    except Exception as e:
                        print(e)
                    globals.SetNewMemberTitle[interaction.user.id] = {}

        button.callback = CB
        view.add_item(button)
        try:
            await ctx.send(f"目前發放稱號為 [{globals.DetectLiveTitleData[str(titleNumber)]['emoji']} {globals.DetectLiveTitleData[str(titleNumber)]['label']}] !!\n限時為 {LimitTime} 分鐘!!", view=view)
        except Exception as e:
            print(e)
        await asyncio.sleep(int(LimitTime) * 60)
        # await asyncio.sleep(10)
        await ctx.send(f"稱號發放已結束!!")
        isLimit = True

        for row in globals.SetNewMemberTitle:
            print(row)
        await SheetFunction.UpdateMemberTitleNumber(titleNumber)


    async def NewTitle(emoji, label, description, ctx):
        try:
            gc = pygsheets.authorize(service_file='./GoogleSheetKey/trusty-fuze-322909-7d29b50ea92c.json')
            sheet = gc.open_by_url('https://docs.google.com/spreadsheets/d/180OzY1HVQw1ucU3w5cqJsHSX5LzbVkonYhfTRzelRJo/edit#gid=0')

            TitleData = sheet.worksheet_by_title("稱號資料")
            SheetData = TitleData.get_all_values()
            non_empty_rows_data = [row[:1] for row in SheetData if any(cell.strip() for cell in row)]
            # print(len(non_empty_rows_data))
            row = [len(non_empty_rows_data), label, emoji, description]
            print(row)

            await ctx.send(f"已新增一個稱號: [{emoji} {label}] !!\n介紹為: {description} ")
            globals.DetectLiveTitleData[str(len(non_empty_rows_data))] = {
                'label':label,
                'emoji':emoji,
                'description':description
            }
            print(globals.DetectLiveTitleData)
            await TitleData.append_table(values=row)
        except Exception as e:
            print(e)

    async def SearchTitleNumber(ctx):
        for row in globals.DetectLiveTitleData:
            await ctx.send(f"({globals.DetectLiveTitleData[row]['emoji']} {globals.DetectLiveTitleData[row]['label']}) 的稱號編號為 {row} 號。")
        
    async def UpdateMemberTitleNumber(TitleNumber):
        try:
            for row in globals.SetNewMemberTitle:
                found = False
                numbers = globals.DetectLiveMemberData[str(row)]['alltitle'].split(",")
                # print(f"1 - {globals.DetectLiveMemberData[str(row)]['alltitle']}")
                # print(f"numbers = {numbers}")
                # print(f"len(numbers) = {len(numbers)}")
                if(numbers[0] == ''):
                    globals.DetectLiveMemberData[str(row)]['alltitle'] = TitleNumber
                    # print(f"2 - {globals.DetectLiveMemberData[str(row)]['alltitle']}")
                else:
                    for number in numbers:
                        if(number == str(TitleNumber)):
                            found = True
                            break
                    if not found:
                        globals.DetectLiveMemberData[str(row)]['alltitle'] += f",{TitleNumber}"
                        # print(f"3 - {globals.DetectLiveMemberData[str(row)]['alltitle']}")
            print(f"a {globals.SetNewMemberTitle}")
            globals.SetNewMemberTitle = {}
            print(f"b {globals.SetNewMemberTitle}")
        except Exception as e:
            print(e)

    async def DirectUpdateMemberTitleNumber(TitleNumber, Member):
        try:
            found = False
            numbers = globals.DetectLiveMemberData[str(Member)]['alltitle'].split(",")
            if(numbers[0] == ''):
                globals.DetectLiveMemberData[str(Member)]['alltitle'] = TitleNumber
            else:
                for number in numbers:
                    if(number == str(TitleNumber)):
                        found = True
                        break
                if not found:
                    globals.DetectLiveMemberData[str(Member)]['alltitle'] += f",{TitleNumber}"
            print(f"稱號新增成功!")
        except Exception as e:
            print(e)

async def setup(bot):
    await bot.add_cog(SheetFunction(bot))


    
    


    










