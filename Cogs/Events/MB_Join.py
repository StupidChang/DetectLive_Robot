from discord.ext import commands
from Global import globals
from Function import SheetFn

class MB_Join(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # @commands.Cog.listener() #當有訊息時
    # async def on_message(self, message):
    #     #print(message)
    #     #print(message.channel)
    #     #排除自己的訊息，避免陷入無限循環
    #     if message.author == self:
    #         return  
    #     if message.content.startswith('你好'):  
    #         await message.channel.send('你好呀OuO')
    #     if message.content.startswith('不好'):
    #         await message.channel.send('你好呀OuO')
    #     await self.process_commands(message)

    @commands.Cog.listener() #當有成員加入時
    async def on_member_join(self, member):

        guild = self.bot.get_guild(int(globals.ServerID))
        # 指定身分組
        role = guild.get_role(int(1091428334220611655))
        # 給予身分組
        await member.add_roles(role)

        print(f"加入新成員: {member}")
        
        SheetFn.SheetFunction.AddNewMemberData2Globals(member.id)
        guild = member.guild
        channel = guild.system_channel
        channel2 = guild.get_channel(int(globals.LiveChannelID))
        welcome_message = (
            f"🔎  歡迎 <@{member.id}> 蒞臨【DetectLive】事務所，這箱沒有很怪。 🔍 \n"
            + f"請參閱 <#1091429875056918679> 以了解事務所規範，歡迎至 <#1065085758882447361> 查詢地圖並登記身分！ \n"
        )
        await channel.send(welcome_message)
        # db_string = "f'" + globals.Welcome_Message + "'"
        # temp = eval(db_string)
        # await channel.send(temp.format(member=member))

async def setup(bot):
    await bot.add_cog(MB_Join(bot))