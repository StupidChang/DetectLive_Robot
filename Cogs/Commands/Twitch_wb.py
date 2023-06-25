from discord.ext import commands
import requests
import websockets
import asyncio
import uuid
import json
from Global import globals
import webbrowser

class Twitch_wb(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def Twitch_wb(self, ctx):
        # mode = 'streamup'
        # callback = 'https://cba8-220-132-121-211.ngrok-free.app/TwitchSub'
        # client_id = 'qz2npqic9tn8sgk5giw96cl5xb6ivk'
        # lease_seconds = 864000
        # secret = 'ywnavcgqvcezlkb9l11im3c9692l2h'

        # headers = {
        #     'Client-ID': client_id,
        #     'Content-type': 'application/json'
        # }

        # topic = f'https://api.twitch.tv/helix/users/follows?first=1&to_id={id}'

        # body = {
        #     'hub.mode': mode,
        #     'hub.topic': topic,
        #     'hub.callback': callback,
        #     'hub.lease_seconds': lease_seconds,
        #     'hub.secret': secret
        # }

        # json_body = json.dumps(body)

        # conn = http.client.HTTPSConnection('api.twitch.tv')
        # conn.request('POST', '/helix/webhooks/hub', body=json_body, headers=headers)

        # response = conn.getresponse()
        # print(response.status, response.reason)
        # print(response.read().decode())

        # conn.close()
        
        webhookurl = "https://api.twitch.tv/helix/webhooks/hub/"
        payload = {
            "hub.mode": "subscribe",
            "hub.topic": "https://api.twitch.tv/helix/users/streams?user_id=27942990",
            "hub.callback": "https://cba8-220-132-121-211.ngrok-free.app/TwitchSub",
            "hub.lease_seconds": "0"
        }
        header = {
            "Content-Type": "application/json",
            "Client-ID": "qz2npqic9tn8sgk5giw96cl5xb6ivk"
        }

        json_payload = json.dumps(payload)
        
        req = requests.post(webhookurl, headers=header, data = json_payload )
        resp = req.json()

        print(resp)
            
async def setup(bot):
    await bot.add_cog(Twitch_wb(bot))