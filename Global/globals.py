from enum import Enum

global Welcome_Message
Welcome_Message = ""

global Roles
Roles = []

global ServerID #DetectLive的伺服器
ServerID = 0

global LiveChannelID #Tag大家開直播的頻道
LiveChannelID = 0

global TwitchLiveChannelID
TwitchLiveChannelID = 0

global streamerAndTag  #直播主和身分組的對應
streamerAndTag = {}

global streamerYtChannelID  #直播主的頻道
streamerYtChannelID = []

global StreamerLiveStatu
StreamerLiveStatu = []

class Level(Enum):
    Diamond = 10000
    Gole = 5000
    Silver = 2000
    Bronze  = 1000
    Iron = 500

global FlaskServer
FlaskServer = None

global DetectLiveMemberData
DetectLiveMemberData = {}

global Response_Code 
Response_Code = None

global Twitchapp
Twitchapp = None

global Client
Client = None

global isStart
isStart = False