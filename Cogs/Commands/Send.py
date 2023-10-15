from discord.ext import commands
from discord.ext import commands, tasks

class Send(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def Send(self, ctx, *, Message):
       # 刪除指令訊息
        await ctx.message.delete()
        
        # 發送消息
        await ctx.send(f"小助手說: {Message}")

async def setup(bot):
    await bot.add_cog(Send(bot)) 