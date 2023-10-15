import asyncio
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime
from discord.ext import commands
from Global import globals

class SetSignIn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.scheduler = None

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def SetSignIn(self, ctx):
        await ctx.send("[系統訊息] - 設定簽到時間為00:00更新")
        self.scheduler = AsyncIOScheduler(timezone="Asia/Taipei")
        self.scheduler.add_job(self.Set, 'cron', hour=0, minute=0)
        self.scheduler.add_job(self.TestTime, 'interval', minutes=60)
        self.scheduler.start()

        print('Schedule started ...')   

        while True:
            await asyncio.sleep(10)  # 暂停 10 秒
            # print('程式執行中...')

    async def Set(self):    
        print("設定簽到時間")
        # await ctx.send("[系統訊息] - 簽到時間為 **[00:00]** ，目前已更新。")
        await ctx.invoke(globals.Client.get_command('YoutubeSub'))
        for row in globals.DetectLiveMemberData:
            print(globals.DetectLiveMemberData[str(row)])
            if globals.DetectLiveMemberData[str(row)]['Signln'] != "TRUE":
                globals.DetectLiveMemberData[str(row)]['SignInDate'] = 0
            globals.DetectLiveMemberData[str(row)]["Signln"] = "FALSE"

    async def TestTime(self):
        print(f'測試啟動: 目前時間{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    

async def setup(bot):
    await bot.add_cog(SetSignIn(bot))   