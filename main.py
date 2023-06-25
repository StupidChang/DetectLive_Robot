import os
from dotenv import load_dotenv
from discord.ext import commands
import discord
from Function import SheetFn
from Global import globals

if __name__ == "__main__":
    global Role
    load_dotenv()
    print(os.getenv('RobotToken'))
    TOKEN = os.getenv('RobotToken')

    #使用client class
    intents = discord.Intents.all()
    intents.message_content = True
    Client = commands.Bot(command_prefix='+', intents=intents)

    Cogs = ['Cogs.Commands.TestLoading',
            'Cogs.Commands.StartBackUp',
            'Cogs.Commands.CheckMemberData',
            'Cogs.Commands.MemberData',
            'Cogs.Commands.RequireData',
            'Cogs.Commands.GetChannelID',
            'Cogs.Commands.Level',
            'Cogs.Commands.webhook',
            'Cogs.Commands.SetWelcomeMessage', 
            'Cogs.Commands.SetReactionRole',
            'Cogs.Commands.DeleteReactionRole', 
            'Cogs.Commands.Twitch', 
            'Cogs.Commands.Twitch_wb',
            'Cogs.Commands.Help', 
            'Cogs.Commands.SetStreamerData',
            'Cogs.Commands.AddExperience',

            'Cogs.Events.on_message', 
            'Cogs.Events.SetRole', 
            'Cogs.Events.RemoveRole', 
            'Cogs.Events.MB_Join', 
            'Cogs.Events.MB_Leave'] # , 'Cogs.Events.LiveTag'

    @Client.command()  
    @commands.has_permissions(administrator=True)
    async def test(ctx):
        print(ctx.message)
        await ctx.send("[系統指令] - 機器人運作中...!")

    @Client.command()  
    @commands.has_permissions(administrator=True)
    async def 開始運作(ctx):
        if not globals.isStart:
            await ctx.invoke(globals.Client.get_command('Start_webhook'))
            await ctx.invoke(globals.Client.get_command('StartBackUp'))
            await ctx.invoke(globals.Client.get_command('runTwitch'))
        else:
            await ctx.send("[系統指令] - 已開啟!")


    @Client.command()  
    @commands.has_permissions(administrator=True)
    async def load(ctx, *args):
        if(len(args) == 0):
            await ctx.send("[系統指令] - 請輸入參數! 範例:+load all")
        else:
            if(args[0] == "all"):
                for Cog in Cogs:
                    try:
                        await Client.load_extension(Cog)
                    except Exception as e:
                        await ctx.send(e)
                await ctx.send("已載入所有函式庫...!")

            elif( len(args) > 0):   
                try:
                    await Client.load_extension(f"Cogs.{args[0]}")
                    await ctx.send(f"[  {args[0]}  ]已載入至函式庫...!")
                except Exception as e:
                    await ctx.send(e)
                
    @Client.command()  
    @commands.has_permissions(administrator=True)
    async def unload(ctx, *args):
        if(len(args) == 0):
            await ctx.send("[系統指令] - 請輸入參數! 範例:+unload something")
        else:
            if(args[0] == "all"):
                for Cog in Cogs:
                    try:
                        await Client.unload_extension(Cog)
                    except Exception as e:
                        await ctx.send(e)
                await ctx.send("[系統指令] - 已解除所有函式庫...!")

            elif( len(args) > 0):
                try:
                    await Client.unload_extension(f"Cogs.{args[0]}")
                    await ctx.send(f"[系統指令] - [  {args[0]}  ]已解除於函式庫...!")
                except Exception as e:
                    await ctx.send(e)

    @Client.command()  
    @commands.has_permissions(administrator=True)
    async def reload(ctx, *args):
        if(len(args) == 0):
            await ctx.send("[系統指令] - 請輸入參數! 範例:+reload something")
        else:
            if(args[0] == "all"):
                for Cog in Cogs:
                    try:
                        await Client.reload_extension(Cog)
                    except Exception as e:
                        await ctx.send(e)
                await ctx.send("[系統指令] - 已進行函式庫重載...!")

            elif( len(args) > 0):
                try:
                    await Client.reload_extension(f"Cogs.{args[0]}")
                    await ctx.send(f"[系統指令] - [  {args[0]}  ]已重載入函式庫...!")
                except Exception as e:
                    await ctx.send(e)

    @Client.command()  
    @commands.has_permissions(administrator=True)
    async def CheckCogs(ctx, *args):
        await ctx.send("---以下為預設載入指令名單---")
        for Cog in Cogs:
            await ctx.send(Cog)
        await ctx.send("---結束---")
        await ctx.send("[如需新增預設載入，請於主程式中修改]")

    #調用event函式庫
    @Client.event #當機器人完成啟動時
    async def on_ready():
        print('目前登入身份：', Client.user)

        game = discord.Game('管理DetectLive中...\n 擔任要職 - [管家]')
        await Client.change_presence(status=discord.Status.idle, activity = game)

        SheetFn.GetRole()  #從Google Sheet取得目前的表情設定並儲存
        SheetFn.GetServerID()
        SheetFn.GetTagLiveChannel()
        SheetFn.GetWelcomeMessage()
        SheetFn.GetStreamerLiveData()
        SheetFn.GetMemberDataFromSheet()
        # print(globals.Roles)

        # print(Client)
        
        for guild in Client.guilds:
            await guild.webhooks()
            # print(f"[{guild}]") #米兔醬 的伺服器
            # print(f"[{guild.me}]") #TestRobot#7918
            channel = guild.system_channel
            await channel.send("DetectLive最可愛的管家機器人已上線(ヾﾉ･ω･`)!")
            
            if(guild.name == "米兔醬 的伺服器"):
                for Cog in Cogs:
                    try:
                        await Client.load_extension(Cog)
                    except Exception as e:
                        await channel.send(e)
                await channel.send("已載入所有函式庫...!")

            #以下為在所有伺服器中的第一個有權限的文字頻道輸出，不是預設頻道
            # for channel in guild.text_channels: #getting only text channels
            #     if channel.permissions_for(guild.me).send_messages: #checking if you have permissions
            #         await channel.send("可愛的機器人已上線!")
            #         break #breaking so you won't send messages to multiple channels

    # 载入 event 和 commands 
    globals.Client = Client
    globals.Client.run(TOKEN)