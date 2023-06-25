from discord.ext import commands
import sys
sys.path.append('../../discordrRobot')
from Function import SheetFn

class SetReactionRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['SRR'])
    @commands.has_permissions(administrator=True)
    async def SetReactionRole(self, ctx, *args):
        if(len(args) == 3):
            await SheetFn.InsertRole(args[0], args[1], args[2])

async def setup(bot):
    await bot.add_cog(SetReactionRole(bot)) 