from discord.ext import commands

class MB_Leave(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener() #當有成員離開時
    async def on_member_remove(self, member):
        guild = member.guild
        channel = guild.system_channel
        await channel.send(f"緬懷 {member.name} 的離開...")
    # 其他事件

async def setup(bot):
    await bot.add_cog(MB_Leave(bot))