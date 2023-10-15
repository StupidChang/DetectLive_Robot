from discord.ext import commands
from Function import SheetFn
from Global import globals

class AddExperience(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def AddExperience(self, ctx):
        globals.DetectLiveMemberData[str(ctx.message.author.id)]['Exp'] = int(1000)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def SetLevel(self, ctx, *args):
        globals.DetectLiveMemberData[str(ctx.message.author.id)]['Level'] = int(args[0])

async def setup(bot):
    await bot.add_cog(AddExperience(bot))