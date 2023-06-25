from discord.ext import commands
from Function import SheetFn

class RequireData(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def RequireData(self, ctx, *args):
        SheetFn.UpdateMemberData2Sheet()

        SheetFn.GetRole()  #從Google Sheet取得目前的表情設定並儲存
        SheetFn.GetServerID()
        SheetFn.GetTagLiveChannel()
        SheetFn.GetWelcomeMessage()
        SheetFn.GetStreamerLiveData()
        SheetFn.GetMemberDataFromSheet()
        await ctx.send("[系統指令] - 已重新取得資料庫資料...")

async def setup(bot):
    await bot.add_cog(RequireData(bot))