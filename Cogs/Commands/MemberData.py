from discord.ext import commands
from Global import globals

class MemberData(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def MemberData(self, ctx):
        print("---目前已在名單中的成員---")
        for member in globals.DetectLiveMemberData:
            print(f"ID: {member}")
        print("---結束---")

async def setup(bot):
    await bot.add_cog(MemberData(bot))