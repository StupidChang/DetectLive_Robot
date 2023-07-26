from discord.ext import commands
import xml
from Global import globals
import xmltodict
import yaml
from quart import Quart, websocket, request
from discord_webhook import DiscordWebhook
from quart import make_response
import json
import asyncio
from Function import SheetFn

class webhook(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # 將 Flask 伺服器的路由設置為機器人的命令
    @commands.command(aliases=['STWH'])
    @commands.has_permissions(administrator=True)
    async def ServerRun(self, ctx):
        app = Quart(__name__)

        # try:
        #     with open("./FlaskServer/config.yaml") as f:
        #         config = yaml.load(f, Loader=yaml.FullLoader)
        # except FileNotFoundError:
        #     print("Unable to load config file: 'config.yaml'")
        #     print("Exiting...")
        #     exit(1)

        @app.route("/feed", methods=["GET", "POST"])
        async def feed():
           
            """Accept and parse requests from YT's pubsubhubbub.
            https://developers.google.com/youtube/v3/guides/push_notifications
            """

            challenge = request.args.get("hub.challenge")
            if challenge:
                print(challenge)
                # YT will send a challenge from time to time to confirm the server is alive.
                return challenge

            try:
                xml_dict = xmltodict.parse(await request.data)
                print(xml_dict)
                if("entry" in xml_dict["feed"]):
                    # channel_id = xml_dict["feed"]["entry"]["yt:channelId"]
                    videoo_id = xml_dict["feed"]["entry"]["yt:videoId"]
                    # if config["channel_ids"] != [] and channel_id not in config["channel_ids"]:
                        # return "", 403

                    # Parse out the video URL.
                    video_url = xml_dict["feed"]["entry"]["link"]["@href"]
                    print(f"New video URL: {video_url}")

                    Name = xml_dict["feed"]["entry"]["author"]["name"]
                    # Name = xml_dict["feed"]["entry"]["author"]["name"]

                    # await asyncio.sleep(2)

                    # live_streams_response = youtube.search().list(
                    #     channelId=channel_id,
                    #     part='snippet',
                    #     eventType='live',
                    #     type='video'
                    # ).execute()
                    
                    await SheetFn.SheetFunction.SearchYoutubeStreamStatus(Name, video_url, videoo_id, ctx)
                    # print(f"response = {response}")
                    # # print(f"live_streams_response = {live_streams_response}")
                    # if 'items' in response:
                    #     video_info = response['items'][0]
                    #     if 'liveStreamingDetails' in video_info:
                    #         if 'actualEndTime' not in video_info['liveStreamingDetails']:
                    #             if 'actualStartTime' in video_info['liveStreamingDetails']:
                    #                 channel2 = ctx.guild.get_channel(int(globals.LiveChannelID))
                    #                 for row in globals.StreamerLiveStatu:
                    #                     # print(row[0])
                    #                     # print(Name)
                    #                     # print(row[0] == Name)
                    #                     if row[0] == Name:
                    #                         TagMessage = (
                    #                                         f"🔴 {Name}直播中...\n"
                    #                                         f"<@&{row[3]}> 正在直播!!\n"
                    #                                         f"{video_url}\n"
                    #                                     )
                    #                         await channel2.send(TagMessage)
                    #             else:
                    #                 globals.VideoStatus[videoo_id] = {}


                    # if live_streams_response['items']:
                        # for item in live_streams_response['items']:
                            # if(item['id']['videoId'] == videoo_id):
                                # print(f"頻道名稱: {Name}")
                                # await ctx.send(f"New video URL: {video_url}")
                                    

                    # channel = ctx.guild.system_channel
                    # await channel.send(TagMessage)

                    # Send the message to the webhook URL.
                    # https://discord.com/developers/docs/resources/webhook

                    # # Discord Webhook 機器人發送
                    # message = config["message_prefix"] + "\n" + video_url
                    # webhook = DiscordWebhook(url=config["webhook_url"], content=message)
                    # response = webhook.execute()

            except (xml.parsers.expat.ExpatError, LookupError):
                # request.data contains malformed XML or no XML at all, return FORBIDDEN.
                return "", 403

                # Everything is good, return NO CONTENT.
            return "", 204
        
        @app.route("/callback", methods=["GET", "POST"])
        async def callback():
            authorization_code = request.args.get('code')
            print(f"Twitch - 回傳 Code : {authorization_code}")
            if authorization_code:
                # 處理授權碼的相關邏輯
                globals.Response_Code = authorization_code
                if(globals.Twitchapp.get_access_token()):
                    globals.Twitchapp.Webhook_sub()
                    # connection = await globals.Twitchapp.connect()
                    # await globals.Twitchapp.heartbeat(connection)
                    # await globals.Twitchapp.receiveMessage(connection)
                # 創建回應對象
                response = make_response(authorization_code)
                return await response  # 使用 await 等待回應的返回
            else:
                # 處理授權失敗的情況

                # 創建回應對象
                response = make_response("授權失敗")
                return await response  # 使用 await 等待回應的返回

        @app.route("/TwitchSub", methods=["GET", "POST"])
        async def TwitchSub():
            xml_data = await request.data
            data_str = xml_data.decode('utf-8')
            data_dict = json.loads(data_str)
            # xml_dict = xmltodict.parse(xml_data)
            print(f"Twitch Data - {data_dict}")
            # print(f"Twitch {data_dict['event']['type']}")
            # print(f"Twitch {data_dict['event']['broadcaster_user_name']}")
            # print(f"Twitch Challenge - {data_dict['challenge']}")
            # print(f"Twitch Request - {request}")
            if 'challenge' in data_dict:
                challenge = data_dict['challenge']
                if challenge:
                    print("Twitch - 開始進行挑戰")
                    return challenge
            else:
                print('Twitch - 此不是挑戰')

            if(data_dict['event']['type'] == "live"):
                for row in globals.StreamerLiveStatu:
                    if(row[2] == data_dict['event']['broadcaster_user_login']):
                        # print(f"globals.LiveChannelID: {globals.LiveChannelID}")

                        channel = ctx.guild.get_channel(int(globals.LiveChannelID))

                        TagMessage = (
                                        f"🔴 {data_dict['event']['broadcaster_user_name']}直播中...\n"
                                        f"<@&{row[4]}> 正在直播!!\n"
                                        f"https://www.twitch.tv/{data_dict['event']['broadcaster_user_login']}\n"
                                    )
                        
                        await channel.send(TagMessage)

            response = make_response("OK")
            return await response

        self.bot.loop.create_task(app.run_task())
        await ctx.send("[系統指令] - 已啟動Quart Server")

    # 在 Flask 伺服器啟動後，可以使用機器人來停止它
    # @commands.command()
    # @commands.has_permissions(administrator=True)
    # async def stop_webhook(self, ctx):

async def setup(bot):
    await bot.add_cog(webhook(bot)) 


