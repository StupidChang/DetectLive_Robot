from discord.ext import commands
from Function import SheetFn
from Global import globals

class SetNgrokLocal(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def SetNgrokLocal(self, ctx, *args):
        globals.NgrokLocal = args[0]
        await ctx.send(f"[系統訊息] - 已成功設定NgrokLocal為 {args[0]}")

async def setup(bot):
    await bot.add_cog(SetNgrokLocal(bot))