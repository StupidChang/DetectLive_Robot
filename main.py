import os
from dotenv import load_dotenv
from discord.ext import commands
import discord

if __name__ == "__main__":
    load_dotenv()
    print(os.getenv('RobotToken'))
    TOKEN = os.getenv('RobotToken')

    #使用client class
    intents = discord.Intents.all()
    intents.message_content = True
    Client = commands.Bot(command_prefix='+', intents=intents)

    Cogs = ['Cogs.Commands', 'Cogs.Events']
    #Client.load_extension("CommandsCog")
    #Client.load_extension("EventsCog")

    @Client.command()  
    async def test(ctx):
        print(ctx.message)
        await ctx.send("指令測試正常!")

    @Client.command()  
    async def load(ctx, *args):
        if(len(args) == 0):
            await ctx.send("請輸入參數! 範例:+load all")
        else:
            if(args[0] == "all"):
                for Cog in Cogs:
                    try:
                        await Client.load_extension(Cog)
                    except Exception as e:
                        await ctx.send(e)
                await ctx.send("載入函式庫完成...!")
                
            elif( len(args) > 0):
                await Client.load_extension(f"Cogs.{args[0]}")

    @Client.command()  
    async def unload(ctx, *args):
        if(len(args) == 0):
            await ctx.send("請輸入參數! 範例:+unload something")
        else:
            await Client.unload_extension(f"Cogs.{args[0]}")
            
            

    #調用event函式庫
    @Client.event #當機器人完成啟動時
    async def on_ready():
        print('目前登入身份：', Client.user)
        print(Client)
        
        for guild in Client.guilds:
            print(guild) #米兔醬 的伺服器
            print(guild.me) #TestRobot#7918
            channel = guild.system_channel
            await channel.send("可愛的機器人已上線!")

            #以下為在所有伺服器中的第一個有權限的文字頻道輸出，不是預設頻道
            # for channel in guild.text_channels: #getting only text channels
            #     if channel.permissions_for(guild.me).send_messages: #checking if you have permissions
            #         await channel.send("可愛的機器人已上線!")
            #         break #breaking so you won't send messages to multiple channels

    # 载入 event 和 commands 

    Client.run(TOKEN)