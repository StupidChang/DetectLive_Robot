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
        print(f"加入新成員: {member}")
        SheetFn.AddNewMemberData2Globals(member.id)
        guild = member.guild
        channel = guild.system_channel
        welcome_message = (
            f"歡迎 {member.name} 的加入...!\n"
            "想要查看Roku的頻道請點擊<:Roku:1108454569157079090>的表情符號!!\n"
            "想要查看123的頻道請點擊<:Roku:1108454569157079090>的表情符號!!\n"
        )
        db_string = "f'" + globals.Welcome_Message + "'"
        temp = eval(db_string)
        await channel.send(temp.format(member=member))

async def setup(bot):
    await bot.add_cog(MB_Join(bot))