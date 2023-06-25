from discord.ext import commands
from Global import globals

class setRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, ctx):
        print(globals.Roles)
        for Role in globals.Roles:
            # print("in")
            # print(ctx.message_id)
            # print(ctx.emoji.name)
            # print(Role[0])
            # print(Role[1])
            # print(Role[2])
            if str(ctx.message_id) == Role[0] and ctx.emoji.name == Role[1]:
                print("1")
                # 取得伺服器
                guild = self.bot.get_guild(ctx.guild_id)
                # 指定身分組
                role = guild.get_role(int(Role[2]))
                # 取得使用者
                user = guild.get_member(ctx.user_id)
                # 給予身分組
                await user.add_roles(role)
                # 傳送私訊給使用者
                # await user.send(f"你取得了{role.name}身分組")
                return

async def setup(bot):
    await bot.add_cog(setRole(bot))