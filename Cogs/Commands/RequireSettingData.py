from discord.ext import commands
from Function import SheetFn

class RequireSettingData(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def RequireSettingData(self, ctx, *args):
        SheetFn.SheetFunction.GetRole()  #從Google Sheet取得目前的表情設定並儲存
        SheetFn.SheetFunction.GetServerID()
        SheetFn.SheetFunction.GetTagLiveChannel()
        SheetFn.SheetFunction.GetWelcomeMessage()
        SheetFn.SheetFunction.GetStreamerLiveData()
        # SheetFn.SheetFunction.GetMemberDataFromSheet()
        SheetFn.SheetFunction.GetTitle()

        await ctx.send("[系統訊息] - 已重新取得 **[設定類別]** 資料庫資料...")

async def setup(bot):
    await bot.add_cog(RequireSettingData(bot))