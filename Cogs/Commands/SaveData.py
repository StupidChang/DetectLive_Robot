from discord.ext import commands
from Function import SheetFn

class SaveData(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def SaveData(self, ctx):
        print("[系統訊息] - 立即開始更新成員資料")
        await ctx.send("[系統訊息] - 立即開始更新成員資料")
        await SheetFn.SheetFunction.CheckMemberData2Sheet()
        await SheetFn.SheetFunction.UpdateMemberData2Sheet()
        await ctx.send("[系統訊息] - 結束更新成員資料")
        print("[系統訊息] - 結束更新成員資料")
 
async def setup(bot):
    await bot.add_cog(SaveData(bot))