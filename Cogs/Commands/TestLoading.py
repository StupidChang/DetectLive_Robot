from discord.ext import commands

class TestLoading(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['TL'])
    @commands.has_permissions(administrator=True)
    async def TestLoading(self, ctx):
        print("Test!!!")
        await ctx.send('函式庫指令已被成功載入!')
        # await ctx.send('<@&1107988906860875786>!')
        # await ctx.send('<:Roku:>!')

async def setup(bot):
    await bot.add_cog(TestLoading(bot))