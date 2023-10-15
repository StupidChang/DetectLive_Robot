import asyncio
from discord.ext import commands
from Function import SheetFn
from Global import globals
import pygsheets

class TempCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command() 
    @commands.has_permissions(administrator=True)
    async def update(self, ctx):
        for row in globals.DetectLiveMemberData:
            print(globals.DetectLiveMemberData[str(row)])
            if globals.DetectLiveMemberData[str(row)]['Signln'] != "TRUE":
                globals.DetectLiveMemberData[str(row)]['SignInDate'] = 0
            globals.DetectLiveMemberData[str(row)]["Signln"] = "FALSE"

    @commands.command() 
    @commands.has_permissions(administrator=True)
    async def Sec(self, ctx):
        print(globals.SetNewMemberTitle)

    @commands.command() 
    @commands.has_permissions(administrator=True)
    async def AddTitle(self, ctx, *args):
        globals.SetNewMemberTitle[args[0]] = {}
        print(globals.SetNewMemberTitle)

    @commands.command() 
    @commands.has_permissions(administrator=True)
    async def SendNewTitle(self, ctx, *args):
        await SheetFn.SheetFunction.UpdateMemberTitleNumber(args[0])

    @commands.command() 
    @commands.has_permissions(administrator=True)
    async def Member(self, ctx, *args):
        print(globals.DetectLiveMemberData[args[0]])

    @commands.command() 
    @commands.has_permissions(administrator=True)
    async def Test(self, ctx, *args):
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

    @commands.command() 
    @commands.has_permissions(administrator=True)
    async def Test2(self, ctx, *args):
        globals.DetectLiveMemberData[str(args[0])]['Exp'] = 100
        print(globals.DetectLiveMemberData[str(args[0])])
    
    @commands.command() 
    @commands.has_permissions(administrator=True)
    async def SetMemberImage(self, ctx, *args):
        globals.DetectLiveMemberData[str(ctx.message.author.id)]['image_url'] = str(args[0])
        
    @commands.command() 
    @commands.has_permissions(administrator=True)
    async def SetStreamer(self, ctx, *args):
        globals.VideoStatus[str(args[0])] = { 
            # "Name":row[0],
            "ChannelID":str(args[1]),
            "VideoURL":str(args[2]),
            "StreamStatus":"False"
        }   
        
    @commands.command() 
    @commands.has_permissions(administrator=True)
    async def StreamerStatus(self, ctx, *args):
        print(globals.VideoStatus)

async def setup(bot):
    await bot.add_cog(TempCommands(bot))