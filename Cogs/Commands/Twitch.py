from discord.ext import commands
import requests
import websockets
import asyncio
import uuid
import json
from Global import globals
import webbrowser

class TwitchWebsocket():
    def __init__(self):
        self.topics = ["channel-bits-events-v1.91967953"]
        self.auth_token = ""
        self.app_auth_token = ""
        self.client_id = "qz2npqic9tn8sgk5giw96cl5xb6ivk"
        self.client_secret = "ywnavcgqvcezlkb9l11im3c9692l2h"
        pass

    async def connect(self):
        '''
           連接到 WebSocket 伺服器
           websockets.client.connect 返回一個 WebSocketClientProtocol，用於發送和接收訊息
        '''
        self.connection = await websockets.connect('wss://pubsub-edge.twitch.tv')
        if self.connection.open:
            print('連接建立。客戶端已成功連接')
            print(self.auth_token)
            # 發送問候語
            message = {"type": "LISTEN", 
                       "nonce": str(self.generate_nonce()), 
                       "data":{
                           "topics": self.topics, 
                           "auth_token": self.auth_token
                           }
                        }
            json_message = json.dumps(message)
            print(json_message)
            await self.sendMessage(json_message)    
            return self.connection  

    def generate_nonce(self):
        '''生成偽隨機數和自紀元（UTC）以來的秒數。'''
        nonce = uuid.uuid1()
        oauth_nonce = nonce.hex
        return oauth_nonce

    async def sendMessage(self, message):
        '''發送訊息到 WebSocket 伺服器'''
        await self.connection.send(message)

    async def receiveMessage(self, connection):
        '''接收所有伺服器訊息並處理它們'''
        while True:
            try:
                message = await connection.recv()
                print('從伺服器收到訊息：' + str(message))
            except websockets.exceptions.ConnectionClosed:
                print('[receiveMessage] 與伺服器的連接關閉')
                break

    async def heartbeat(self, connection):
        '''
        每分鐘向伺服器發送心跳訊號
        使用 Ping-Pong 訊號來驗證/保持連接存活
        '''
        while True:
            try:
                data_set = {"type": "PING"}
                json_request = json.dumps(data_set)
                print(f"data_set = {json_request}")
                await self.connection.send(json_request)
                await asyncio.sleep(60)
            except websockets.exceptions.ConnectionClosed:
                print('[heartbeat] 與伺服器的連接關閉')
                break

    def get_twitch_code(self):
        # Step 1: Request an authorization code from the user
        url = "https://id.twitch.tv/oauth2/authorize"
        payload_code = {
            "response_type": "code",
            "client_id": "qz2npqic9tn8sgk5giw96cl5xb6ivk",
            "redirect_uri": "https://cba8-220-132-121-211.ngrok-free.app/callback",
            "scope": "channel%3Amanage%3Apolls+channel%3Aread%3Apolls",
            "state": "c3ab8aa609ea11e793ae92361f002671"
        }
        
        authorization_url = url + "?" + "&".join(f"{key}={value}" for key, value in payload_code.items())
        # 打开授权页面供用户登录和授权
        webbrowser.open(authorization_url)

    def get_access_token(self):
        # Step 2: Exchange authorization code for access token
        print(globals.Response_Code)
        url = "https://id.twitch.tv/oauth2/token"
        payload = {
            "client_id": "qz2npqic9tn8sgk5giw96cl5xb6ivk",
            "client_secret": "ywnavcgqvcezlkb9l11im3c9692l2h",
            "code": globals.Response_Code,
            "grant_type": "authorization_code",
            "redirect_uri": "https://cba8-220-132-121-211.ngrok-free.app/callback"
        }
        response = requests.post(url, data=payload)
        print(f"請求Twitch access_token 訪問令牌 : {response.text}")
        if response.status_code == 200:
            print("Twitch - success to get access token")
            access_token = response.json()["access_token"]
            print(f"Twitch - access_token is {access_token}")
            self.auth_token = access_token
            return True
        else:
            print("Twitch - Failed to get access token")
            self.auth_token = None
            return False
        
    def get_app_access_token(self):
        print("Twitch - 取得APP access Token")
        url = 'https://id.twitch.tv/oauth2/token'
        params = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': 'client_credentials'
        }
        response = requests.post(url, params=params)
        if response.status_code == 200:
            data = response.json()
            self.app_auth_token = data['access_token']
            print("Twitch - 取得APP access Token 成功")
            return True
        else:
            print(response.json())
            print("Twitch - 取得APP access Token 失敗")
            return False

    def Webhook_sub(self):
        print("Twitch - 開始註冊Twitch Webhook")
        print(f"app token is {self.app_auth_token}")

        for row in globals.StreamerLiveStatu:
            if(row[3] != ""):
                print(row)

                url = "https://api.twitch.tv/helix/eventsub/subscriptions"
                payload = {
                    'type': "stream.online",
                    'version': '1',
                    'condition': {
                        'broadcaster_user_id': row[3]
                    },
                    'transport': {
                        'method': 'webhook',
                        'callback': f"{globals.NgrokLocal}/TwitchSub",
                        'secret': "ywnavcgqvcezlkb9l11im3c9692l2h"
                    }
                }

                # webhookurl = "https://api.twitch.tv/helix/webhooks/hub/"
                # payload = {
                #     "hub.mode": "subscribe",
                #     "hub.topic": "https://api.twitch.tv/helix/users/streams?user_id=27942990",
                #     "hub.callback": "https://cba8-220-132-121-211.ngrok-free.app/TwitchSub",
                #     "hub.lease_seconds": "0"
                # }

                header = {
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {self.app_auth_token}",
                    "Client-ID": "qz2npqic9tn8sgk5giw96cl5xb6ivk"
                }

                json_payload = json.dumps(payload)
                
                req = requests.post(url, headers=header, data = json_payload )
                resp = req.json()

                print(f"Twitch - 註冊結果為 {resp}")
        

class Twitch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(aliases=[''])
    @commands.has_permissions(administrator=True)
    async def TwitchSub(self, ctx):
        globals.Twitchapp = TwitchWebsocket()
        if(globals.Twitchapp.get_app_access_token()):
            globals.Twitchapp.Webhook_sub()
            await ctx.send("[系統指令] - 已向Twitch註冊直播主")

        # globals.Twitchapp.get_twitch_code()

        # print(asyncio.get_running_loop())
        # Start connection and get client connection protocol
        # connection = self.bot.loop.run_until_complete(client.connect())
        # # Start listener and heartbeat
        # tasks = [
        #     asyncio.ensure_future(client.heartbeat(connection)),
        #     asyncio.ensure_future(client.receiveMessage(connection)),
        # ]

        # self.bot.loop.run_until_complete(asyncio.wait(tasks))

    # async def Twitch(self, ctx, *args):
    #     client_id = "qz2npqic9tn8sgk5giw96cl5xb6ivk"
    #     headers = {
    #         "Client-ID": client_id
    #     }
    #     response = requests.get("https://api.twitch.tv/helix/streams", headers=headers, params={"user_login": "YOUR_TWITCH_CHANNEL_LOGIN"})

            
async def setup(bot):
    await bot.add_cog(Twitch(bot))