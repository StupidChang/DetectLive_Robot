from discord.ext import commands
from Function import SheetFn
from discord.ext import commands, tasks
from Global import globals

class StartBackUp(commands.Cog):
    def __init__(self, bot):
        self.run = False
        self.bot = bot
        self.BackUp.start()
        self.Set.start()

    @commands.command(aliases=['SBU'])
    @commands.has_permissions(administrator=True)
    async def StartBackUp(self, ctx):
        if not self.run:
            if not globals.isStart:
                await ctx.send("[系統指令] - 啟動自動備份...每1小時進行儲存")
                globals.isStart = True
                self.run = True
                
        
    @tasks.loop(minutes=60)
    async def BackUp(self):
        if(self.run):
            print("開始執行備份")
            await SheetFn.UpdateMemberData2Sheet()
        
    @tasks.loop(minutes=1440)
    async def Set(self):    
        if(self.run):
            print("設定簽到時間")
            for row in globals.DetectLiveMemberData:
                print(globals.DetectLiveMemberData[str(row)])
                globals.DetectLiveMemberData[str(row)]["Signln"] = "FALSE"

async def setup(bot):
    await bot.add_cog(StartBackUp(bot)) 