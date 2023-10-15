from discord.ext import commands
from Global import globals

class setRole(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        # print(globals.Roles)
        for Role in globals.Roles:
            # print("in")
            # print(ctx.message_id)
            # print(ctx.emoji.name)
            # print(Role[0])
            # print(Role[1])
            # print(Role[2])
            # print(payload.message_id)
            # print(Role[0]) 
            # print(str(payload.emoji.name))
            # print(Role[1])
            # print(str(payload.emoji.name) == Role[1])
            if str(payload.message_id) == Role[0] and payload.emoji.name == Role[1]:
                # 取得伺服器
                guild = self.bot.get_guild(payload.guild_id)
                # 取得使用者
                user = guild.get_member(payload.user_id)

                if payload.emoji.name == "💮":
                    try:
                        role2 = guild.get_role(int(1091428334220611655))
                        await user.remove_roles(role2)
                    except:
                        print("刪除錯誤")
                
                # 指定身分組
                role = guild.get_role(int(Role[2]))
                
                # 給予身分組
                await user.add_roles(role)
                
                # 傳送私訊給使用者
                # await user.send(f"你取得了{role.name}身分組")
                return

async def setup(bot):
    await bot.add_cog(setRole(bot))