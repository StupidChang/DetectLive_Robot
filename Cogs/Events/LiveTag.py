import discord
import datetime
from googleapiclient.discovery import build
from discord.ext import commands, tasks
from Global import globals

class LiveTag(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.check_streamer.start()

    def cog_unload(self):
        self.check_streamer.cancel()

    @tasks.loop(minutes=1)
    async def check_streamer(self):
        guild = self.bot.get_guild(int(globals.ServerID))  # 利用ID取得伺服器
        liveChannel = guild.get_channel(int(globals.LiveChannelID)) # 利用ID取的伺服器中的頻道
        # print("globals.LiveChannelID為  " + globals.LiveChannelID)
        youtube = build('youtube', 'v3', developerKey="AIzaSyBdXrPPQN2BEelDvWsW_h9Rxtwi0eas79I")

        # 搜尋直播主的頻道 ID
        # channels_response = youtube.videos().list(
        #     id='X9zw0QF12Kc',
        #     part='snippet',
        #     # type='channel'
        # ).execute()
        # print(f"channelId = {channels_response['items'][0]['snippet']['channelId']}") 
        for Streamer in globals.StreamerLiveStatu:
            print()
            
        if(True == True):
            # 搜尋直播中的影片
            live_streams_response = youtube.search().list(
                channelId='UC-hM6YJuNYVAmUWxeIr9FeA',
                part='snippet',
                eventType='live',
                type='video'
            ).execute()

            if(len(live_streams_response) == 0):
                # 搜尋即將直播的影片
                upcoming_streams_response = youtube.search().list(
                    channelId='UC-hM6YJuNYVAmUWxeIr9FeA',
                    part='snippet',
                    eventType='upcoming',
                    type='video'
                ).execute()
                # print(f"VideoID = {upcoming_streams_response}")
                VideoID = upcoming_streams_response['items'][0]['id']['videoId']
                LiveStreamDate = youtube.videos().list(
                    id=VideoID,
                    part='liveStreamingDetails',
                    # type='video'
                ).execute()

            print(LiveStreamDate)
            print(f"預定直播時間 = {LiveStreamDate['items'][0]['liveStreamingDetails']['scheduledStartTime']}")

            if(len(live_streams_response['items']) > 0):
                if(Streamer[3] == False):
                    TagMessage = (
                                f"🔴 {Streamer[0]}直播中...\n"
                                f"<@&{Streamer[2]}> 正在直播!!\n"
                                f"標題: {live_streams_response['items'][0]['snippet']['title']}\n"
                                f"https://www.youtube.com/watch?v={live_streams_response['items'][0]['id']['videoId']}\n"
                            )
                    Streamer[3] = True
                    await liveChannel.send(TagMessage)
            elif(len(live_streams_response['items']) == 0 and len(upcoming_streams_response['items']) == 0):
                Streamer[3] = False
                Streamer[4] = False
            elif(len(upcoming_streams_response['items']) > 0):
                    if(Streamer[4] == False):
                        # 获取即将直播的视频的开始时间（假设为 upcoming_start_time）
                        # upcoming_start_time = datetime.datetime.strptime(upcoming_streams_response['items'][0]['snippet']['scheduledStartTime'], "%Y-%m-%dT%H:%M:%S%z")
                        # print(f"upcoming_start_time = {upcoming_start_time}")
                        # # 计算当前时间与开始时间之间的时间差
                        # time_difference = upcoming_start_time - current_time
                        TagMessage = (
                                    f"🟠 {Streamer[0]} 即將進行直播...\n"
                                    f"<@&{Streamer[2]}> 直播即將於 {live_streams_response['items'][0]['liveStreamingDetails']['scheduledStartTime']} 開始!!\n"
                                    f"標題: {live_streams_response['items'][0]['snippet']['title']}\n"
                                    f"https://www.youtube.com/watch?v={live_streams_response['items'][0]['id']['videoId']}\n"
                                )
                        Streamer[4] = True
                        await liveChannel.send(TagMessage)

async def setup(bot):
    await bot.add_cog(LiveTag(bot))