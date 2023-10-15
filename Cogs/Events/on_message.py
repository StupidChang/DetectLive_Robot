from discord.ext import commands
from Global import globals

class on_message(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener() #當有訊息時
    async def on_message(self, message):
        # print(message.author.id)
        if message.author == self.bot.user:
            return  
        elif message.content.startswith(self.bot.command_prefix):
            return
        
        # print(message.channel.id)
        # print(globals.ExperienceChannelID)
        # print(str(message.channel.id) in globals.ExperienceChannelID)
        if str(message.channel.id) in globals.ExperienceChannelID:
            try:
                globals.DetectLiveMemberData[str(message.author.id)]['Exp'] += 1
                print("[系統訊息] - 增加成員經驗值成功")
            except:
                print("[系統訊息] - 增加成員經驗值錯誤")

        await self.bot.process_commands(message)

    # @commands.Cog.listen('on_message') #當有訊息時
    # async def whatever_you_want_to_call_it(message):
    #     print(message.author.id)
    #     if message.author == self.bot:
    #         return  
    #     if message.content.startswith('你好'):  
    #         await message.channel.send('你好呀OuO')
    #     if message.content.startswith('不好'):
    #         await message.channel.send('你好呀OuO')
    #     print("2")
    #     await self.bot.process_commands(message)

async def setup(bot):
    await bot.add_cog(on_message(bot))