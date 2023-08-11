from discord.ext import commands
from Function import SheetFn
from discord.ext import commands, tasks
from Global import globals

class StartBackUp(commands.Cog):
    def __init__(self, bot):
        self.run = False
        self.bot = bot
        self.ctx = None
        self.BackUp.start()
        self.Set.start()
        self.CheckYoutubeStreamStatus.start()

    @commands.command(aliases=['SBU'])
    @commands.has_permissions(administrator=True)
    async def StartBackUp(self, ctx):
        if not self.run:
            if not globals.isStart:
                await ctx.send("[系統指令] - 啟動自動備份...每1小時進行儲存")
                globals.isStart = True
                self.run = True
                self.ctx = ctx
        
    @tasks.loop(minutes=60)
    async def BackUp(self):
        if(self.run):
            print("[系統訊息] - 開始執行備份")
            await SheetFn.SheetFunction.SetMemberData2Sheet()
            await SheetFn.SheetFunction.UpdateMemberData2Sheet()
            print("[系統訊息] - 結束執行備份")

    @tasks.loop(minutes=5)
    async def CheckYoutubeStreamStatus(self):
        if(self.run):
            print("開始確認影片直播狀態")
            for VideoID in globals.VideoStatus:
                await SheetFn.SheetFunction.SearchYoutubeStreamStatus(globals.VideoStatus[VideoID]['ChannelID'], globals.VideoStatus[VideoID]['VideoURL'], VideoID, self.ctx)
            for DeleteVideoID in globals.WillBeDelete:
                print(DeleteVideoID)
                del globals.VideoStatus[DeleteVideoID]
            globals.WillBeDelete = []

    @tasks.loop(minutes=1440)
    async def Set(self):    
        if(self.run):
            print("設定簽到時間")
            for row in globals.DetectLiveMemberData:
                print(globals.DetectLiveMemberData[str(row)])
                if globals.DetectLiveMemberData[str(row)]['Signln'] == "TRUE":
                    globals.DetectLiveMemberData[str(row)]['SignInDate'] = 0
                globals.DetectLiveMemberData[str(row)]["Signln"] = "FALSE"

async def setup(bot):
    await bot.add_cog(StartBackUp(bot)) 