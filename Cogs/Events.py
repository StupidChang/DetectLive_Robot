from discord.ext import commands

class EventCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot is ready')

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
        print(member)
        guild = member.guild
        channel = guild.system_channel
        await channel.send("歡迎 {member.name} 的加入...!")

    @commands.Cog.listener() #當有成員離開時
    async def on_member_remove(self, member):
        guild = member.guild
        channel = guild.system_channel
        await channel.send("緬懷 {member.name} 的離開...")
    # 其他事件

async def setup(bot):
    await bot.add_cog(EventCog(bot))