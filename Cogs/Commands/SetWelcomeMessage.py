from discord.ext import commands
import sys
sys.path.append('../../discordrRobot')
from Function import SheetFn

class SetWelcomeMessage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['SWM'])
    @commands.has_permissions(administrator=True)
    async def SetWelcomeMessage(self, ctx, *args):
        if(len(args) == 1):
            print(args[0])
            await SheetFn.SheetFunction.SetWelcomeMessage(args[0])
        else:
            await ctx.send("請輸入設定訊息!")

async def setup(bot):
    await bot.add_cog(SetWelcomeMessage(bot)) 