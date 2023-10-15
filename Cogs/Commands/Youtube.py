from discord.ext import commands
import requests
import websockets
import asyncio
import uuid
import json
from Global import globals
import webbrowser

class Youtube(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def YoutubeSub(self, ctx):
        for row in globals.StreamerLiveStatu:
            if(row[1] != ""):
                mode = 'subscribe'
                callback = f"{globals.NgrokLocal}/feed"
                hub = 'https://pubsubhubbub.appspot.com/subscribe'

                req_data = {
                            "hub.mode": mode,
                            "hub.callback": callback,
                            "hub.lease_seconds": 60*60*24*365,
                            "hub.verify": "async",
                            # "hub.topic": f"https://www.youtube.com/xml/feeds/videos.xml?channel_id=UCAan-j8ovgt85LjIYKHbkdw"
                            "hub.topic": f"https://www.youtube.com/xml/feeds/videos.xml?channel_id={row[1]}",
                        }

                requests.packages.urllib3.disable_warnings()
                try:
                    response = requests.post(hub, data=req_data, verify=False, timeout=10)
                    print(response)
                except requests.exceptions.RequestException as e:
                    print(e)
                    
        await ctx.send("[系統訊息] - 已向Youtube註冊直播主")

async def setup(bot):
    await bot.add_cog(Youtube(bot))