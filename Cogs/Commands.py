from discord.ext import commands

class CommandsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def TestLoading(self, ctx):
        await ctx.send('函式庫指令已被成功載入!')

    # 其他指令

async def setup(bot):
    await bot.add_cog(CommandsCog(bot))