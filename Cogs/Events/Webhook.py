from discord.ext import commands
import requests

class Webhook(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        Webhook()

    async def Webhook(self, ctx):
        mode = 'subscribe'
        callback = 'Your callback url'
        hub = 'https://pubsubhubbub.appspot.com/subscribe'

        req_data = {
                    "hub.mode": mode,
                    "hub.callback": callback,
                    "hub.lease_seconds": 60*60*24*365,
                    "hub.verify": "async",
                    "hub.topic": "https://www.youtube.com/xml/feeds/videos.xml?channel_id=UC-hM6YJuNYVAmUWxeIr9FeA",
                }

        requests.packages.urllib3.disable_warnings()
        try:
            response = requests.post(hub, data=req_data, verify=False, timeout=10)
            print(response)
        except requests.exceptions.RequestException as e:
            print(e)

async def setup(bot):
    await bot.add_cog(Webhook(bot))