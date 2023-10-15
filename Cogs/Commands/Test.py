from discord.ext import commands
from Function import SheetFn
from discord.ext import commands, tasks
from Global import globals

class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['SBU'])
    @commands.has_permissions(administrator=True)
    async def Test(self, ctx):
        await ctx.send(globals.NgrokLocal)

async def setup(bot):
    await bot.add_cog(Test(bot)) 