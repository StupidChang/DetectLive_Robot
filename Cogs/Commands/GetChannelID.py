from discord.ext import commands
from googleapiclient.discovery import build

class GetChannelID(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def GetChannelID(self, ctx, *args):
        if(len(args) > 0):
            youtube = build('youtube', 'v3', developerKey="AIzaSyBdXrPPQN2BEelDvWsW_h9Rxtwi0eas79I")
            responseID = youtube.videos().list(
                id=args[0],
                part='snippet'
                # type='channel'
            ).execute()

            print(f"channelId = {responseID['items'][0]['snippet']['channelId']}") 

            await ctx.send(f"此YT頻道的頻道ID為: [ {responseID['items'][0]['snippet']['channelId']} ]")
            await ctx.send("!!!警告!!! 請勿過度使用此指令，過度使用將造成API資源耗盡!!!")
        else:
            await ctx.send("語法錯誤!")

async def setup(bot):
    await bot.add_cog(GetChannelID(bot))