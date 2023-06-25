from discord.ext import commands
import sys
sys.path.append('../../discordrRobot')
from Function import SheetFn

class DeleteReactionRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def DeleteReactionRole(self, ctx, *args):
        if(len(args) == 3):
            SheetFn.DeleteRole(args[0], args[1], args[2])

async def setup(bot):
    await bot.add_cog(DeleteReactionRole(bot))