from discord.ext import commands
from Function import SheetFn
from discord.ext import commands, tasks
from Global import globals
from datetime import datetime

class StartBackUp(commands.Cog):
    def __init__(self, bot):
        self.run = False
        self.bot = bot
        self.ctx = None
        # self.BackUp.start()
        # self.Set.start()
        # self.CheckYoutubeStreamStatus.start()

    @commands.command(aliases=['SBU'])
    @commands.has_permissions(administrator=True)
    async def StartBackUp(self, ctx):
        try:
            await ctx.send("[系統訊息] - 啟動自動備份...每6小時進行儲存")
            self.BackUp.start()
            globals.isStart = True
        except Exception as e:
            print(f"[備份系統] - {e}")
        
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def StopBackUp(self, ctx):
        await ctx.send("[系統訊息] - 關閉備份")
        self.BackUp.stop()

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def StartCheckYoutubeStream(self, ctx):
        try:
            await ctx.send("[系統訊息] - 開啟確認影片直播狀態")
            self.CheckYoutubeStreamStatus.start()
            self.ctx = ctx 
        except Exception as e:
            print(f"[備份系統] - {e}")
        
    @commands.command()
    @commands.has_permissions(administrator=True)   
    async def StopCheckYoutubeStream(self, ctx):
        await ctx.send("[系統訊息] - 停止確認影片直播狀態")
        self.CheckYoutubeStreamStatus.stop()

    @tasks.loop(minutes=360)
    async def BackUp(self):
        print("[系統訊息] - 開始執行備份")
        await SheetFn.SheetFunction.CheckMemberData2Sheet()
        await SheetFn.SheetFunction.UpdateMemberData2Sheet()
        print("[系統訊息] - 結束執行備份")

    @tasks.loop(minutes=5)
    async def CheckYoutubeStreamStatus(self):
        print("開始確認影片直播狀態")
        for VideoID in globals.VideoStatus:
            await SheetFn.SheetFunction.SearchYoutubeStreamStatus(globals.VideoStatus[VideoID]['ChannelID'], globals.VideoStatus[VideoID]['VideoURL'], VideoID, self.ctx)
        for DeleteVideoID in globals.WillBeDelete:
            try:
                del globals.VideoStatus[DeleteVideoID]
            except Exception as e:
                print(f"[錯誤訊息] - 刪除直播影片ID錯誤! 錯誤訊息為: {e}")
        globals.WillBeDelete = []

    @tasks.loop(minutes=1440)
    async def Set(self):    
        if(self.run):
            print("設定簽到時間")
            for row in globals.DetectLiveMemberData:
                print(globals.DetectLiveMemberData[str(row)])
                if globals.DetectLiveMemberData[str(row)]['Signln'] != "TRUE":
                    globals.DetectLiveMemberData[str(row)]['SignInDate'] = 0
                globals.DetectLiveMemberData[str(row)]["Signln"] = "FALSE"

async def setup(bot):
    await bot.add_cog(StartBackUp(bot)) 