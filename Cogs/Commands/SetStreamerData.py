from discord.ext import commands
from Function import SheetFn
from discord.ext import commands, tasks
from Global import globals

class SetStreamerData(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(aliases=[])
    @commands.has_permissions(administrator=True)
    async def SetStreamerData(self, ctx, *args):
        if(len(args) == 5):
            await SheetFn.SetStreamerLiveData(args[0], args[1], args[2], args[3], args[4])
    
async def setup(bot):
    await bot.add_cog(SetStreamerData(bot)) 