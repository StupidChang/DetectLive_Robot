from discord.ext import commands
from Global import globals

class RemoveRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, ctx):
        for Role in globals.Roles:
            if str(ctx.message_id) == Role[0] and ctx.emoji.name == Role[1]:
                guild = self.bot.get_guild(ctx.guild_id)
                role = guild.get_role(int(Role[2]))
                user = guild.get_member(ctx.user_id)
                await user.remove_roles(role)
                # await user.send(f"你失去了{role.name}身分組")
                return

async def setup(bot):
    await bot.add_cog(RemoveRole(bot))