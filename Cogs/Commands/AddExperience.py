from discord.ext import commands
from Function import SheetFn
from Global import globals

class AddExperience(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def AddExperience(self, ctx):
        globals.DetectLiveMemberData[str(ctx.message.author.id)]['Exp'] = 1000

async def setup(bot):
    await bot.add_cog(AddExperience(bot))