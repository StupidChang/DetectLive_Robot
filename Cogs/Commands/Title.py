from discord.ext import commands
from Function import SheetFn

class Title(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def Title(self, ctx, *args):
        if(len(args) > 0):
            if(args[0] == "New"):
                if(args[1] != None):
                    if(args[2] != None):
                        if(args[3] != None):
                            await SheetFn.SheetFunction.NewTitle(args[1], args[2], args[3], ctx)

            if(args[0] == "Send"):
                if(args[1] != None):
                    if(args[2] != None):
                        await SheetFn.SheetFunction.SendTitle(args[1], args[2], ctx)
                    else:
                        await SheetFn.SheetFunction.SendTitle(args[1], 30, ctx)

            if(args[0] == "Search"):
                if(args[1] != None):
                    await ctx.send(f"此稱號 {args[1]} 的編號為: {SheetFn.SearchTitleNumber(args[1])}")

async def setup(bot):
    await bot.add_cog(Title(bot))