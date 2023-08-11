from discord.ext import commands
import discord
import datetime
from Global import globals
from Function import SheetFn

# class MyModal(discord.ui.Modal, title = "測試"):
#     answer = discord.ui.TextInput(label="HI", placeholder="請輸入簡介",style= discord.TextStyle.short)

#     async def on_submit(self, interaction: discord.Interaction):
#         embed = discord.Embed(title = self.title, description = f"{self.answer.label}**\n{self.answer}", timestamp = datetime.now(), color = discord.Colour.blue())
#         embed.set_author(name = interaction.user, icon_url=interaction.user.avatar)
#         await interaction.response.send_message(embed = embed)    

class Level(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def Rank(self, ctx, *args):
        if(len(args) > 0):
            if(args[0] == "set"):
                if(args[1] != None):
                    globals.DetectLiveMemberData[str(ctx.message.author.id)]['LevelMessage'] = args[1]
                else:
                    await ctx.send("[系統訊息] - 請在set後設定想要在介紹中顯示的文字訊息")
            if(args[0] == "title"):
                # df1 = True if test1_role in interaction.user.roles else False
                # df2 = True if test2_role in interaction.user.roles else False  
                numbers = globals.DetectLiveMemberData[str(ctx.message.author.id)]['alltitle'].split(',')
                print(globals.DetectLiveMemberData[str(ctx.message.author.id)]['alltitle'])
                print(numbers)
                options = []
                for number in numbers:
                    if number in globals.DetectLiveTitleData:
                        option = discord.SelectOption(
                            label=globals.DetectLiveTitleData[number]['label'],
                            emoji=globals.DetectLiveTitleData[number]['emoji'],
                            description=globals.DetectLiveTitleData[number]['description'],
                            value=f"{globals.DetectLiveTitleData[number]['emoji']} {globals.DetectLiveTitleData[number]['label']}",
                            default=False
                        )
                        options.append(option)
                print(options)
                if options == []:
                    await ctx.send("尚未獲得任何稱號!")
                else:
                # options = [
                #     discord.SelectOption(label="[會飛的火龍]", emoji="🐔", description="初始參與第一次活動獲得。", value="🐔 [會飛的火龍]", default=False),
                #     discord.SelectOption(label="[創世者]", emoji="🗽", description="最初支持DetectLive的觀眾", value="🗽 [創世者]", default=False)
                # ]
                    placeholder = f"{ctx.message.author} 請選擇您的稱號!"
                    async def SelectCallback(interaction):
                        if interaction.user.id == ctx.message.author.id:
                            await interaction.response.send_message(f"您選擇了 {select.values[0]} 做為您的稱號!")   
                            globals.DetectLiveMemberData[str(interaction.user.id)]['title'] = select.values[0]

                    select = discord.ui.Select(placeholder=placeholder,options=options)
                    select.callback = SelectCallback
                    view = discord.ui.View()
                    view.add_item(select)
                    await ctx.send(view=view)

        else:
            embed = discord.Embed(
                title=f"DetectLive的資料卡!",
                description=f"➤介紹: \n{globals.DetectLiveMemberData[str(ctx.message.author.id)]['LevelMessage']}",
                color=0x5bbcff  
            )

            # globals.DetectLiveMemberData[str(ctx.message.author.id)]['Exp'] = 273
            # print(globals.DetectLiveMemberData[str(ctx.message.author.id)]['Exp'] / 1000) 

            progressbar = "["
            for i in range(0, 20):
                if((i + 1) <= (globals.DetectLiveMemberData[str(ctx.message.author.id)]['Exp'] / 1000) * 20):
                    progressbar += "■"
                else:
                    progressbar += "-"
            
            progressbar += "]  "
            progressbar += f"({globals.DetectLiveMemberData[str(ctx.message.author.id)]['Exp']} / 1000)"

            embed.set_author(name=ctx.message.author.name, icon_url=ctx.message.author.display_avatar.url)
            embed.add_field(name="📥 [加入伺服器日期]:", value=globals.DetectLiveMemberData[str(ctx.message.author.id)]['JoinServerDate'], inline=True)
            embed.add_field(name="⏱️ [已連續簽到]:", value=f"{globals.DetectLiveMemberData[str(ctx.message.author.id)]['SignInDate']} 天", inline=True) 
            embed.add_field(name="🪪 [目前等級]:", value=globals.DetectLiveMemberData[str(ctx.message.author.id)]['Level'], inline=False)
            embed.add_field(name="🗡️ [經驗值]:", value=progressbar, inline=True) #globals.DetectLiveMemberData[str(ctx.message.author.id)]['Exp']
            embed.add_field(name="📜 [活動參加狀態]:", value=globals.DetectLiveMemberData[str(ctx.message.author.id)]['Activity'], inline=False) #globals.DetectLiveMemberData[str(ctx.message.author.id)]['Exp']
            embed.add_field(name="🎉 [稱號]:", value=globals.DetectLiveMemberData[str(ctx.message.author.id)]['title'], inline=False)   
            embed.set_footer(text='[=- DetectLive所屬製作 -=]')
            embed.set_thumbnail(url="https://img.moegirl.org.cn/common/d/db/BA_Noa_ML.png")
            embed.timestamp = datetime.datetime.now()

            view = discord.ui.View()

            # 第一個按鈕
            if(globals.DetectLiveMemberData[str(ctx.message.author.id)]['Signln'] == "FALSE"):
                button = discord.ui.Button(
                    emoji="🦦",
                    label="簽到",
                    style=discord.ButtonStyle.primary
                )
                async def button_callback(interaction: discord.Interaction):
                    if interaction.user.id == ctx.message.author.id:
                        await interaction.response.defer()

                        channel = interaction.channel
                        message = f"[系統訊息] - {interaction.user.name} 今日已成功簽到！ Exp增加了100點啦♡(*´∀｀*)人(*´∀｀*)♡"
                        await channel.send(message)

                        SheetFn.SheetFunction.AddExp(str(ctx.message.author.id), 100)

                        globals.DetectLiveMemberData[str(ctx.message.author.id)]['Signln'] = "TRUE"
                        # print(globals.DetectLiveMemberData[str(ctx.message.author.id)])
                        # print(globals.DetectLiveMemberData[str(ctx.message.author.id)]['SignInDate'])
                        globals.DetectLiveMemberData[str(ctx.message.author.id)]['SignInDate'] += 1
                        button.disabled = True
                        await interaction.message.edit(view=view)
                    else:
                        await interaction.response.send_message("[系統訊息] - 您無權點擊此按鈕！", ephemeral=True)
                button.callback = button_callback
            else:
                button = discord.ui.Button(
                    emoji="✅",
                    label="今日已簽到",
                    style=discord.ButtonStyle.primary,
                    disabled=True
                )

            # 第二個按鈕
            if(globals.DetectLiveMemberData[str(ctx.message.author.id)]['Exp'] >= 1000):
                button2 = discord.ui.Button(    
                    emoji="⤴️",
                    label="提升等級",
                    style=discord.ButtonStyle.green
                )
                async def button2_callback(interaction: discord.Interaction):
                    if interaction.user.id == ctx.message.author.id:
                        await interaction.response.defer()

                        channel = interaction.channel
                        globals.DetectLiveMemberData[str(ctx.message.author.id)]['Level'] += 1
                        globals.DetectLiveMemberData[str(ctx.message.author.id)]['Exp'] -= 1000
                        message = f"[系統訊息] - {interaction.user.name} 已提升至{globals.DetectLiveMemberData[str(ctx.message.author.id)]['Level']}啦♡(*´∀｀*)人(*´∀｀*)♡"
                        await channel.send(message)

                        button2.disabled = True
                        await interaction.message.edit(view=view)
                    else:
                        await interaction.response.send_message("[系統訊息] - 您無權點擊此按鈕！", ephemeral=True)
                button2.callback = button2_callback
            else:
                button2 = discord.ui.Button(
                    emoji="⛔",
                    label="升級經驗不足",
                    style=discord.ButtonStyle.red,
                    disabled=True
                )

            # 第三個按鈕
            button3 = discord.ui.Button(
                    emoji="📝",
                    label="參加活動",
                    style=discord.ButtonStyle.secondary,
                    disabled=False
                )
            
            async def button3_callback(interaction: discord.Interaction):
                if interaction.user.id == ctx.message.author.id:
                    await interaction.response.defer()
                    # Textinput = discord.ui.TextInput(label="HI", placeholder="請輸入簡介",style= discord.TextStyle.short)
                    # ModalView.add_item(Textinput)
                    # A = MyModal()
                    # await interaction.response.send_modal(A)
                else:
                    await interaction.response.send_message("[系統訊息] - 您無權點擊此按鈕！", ephemeral=True)
            button3.callback = button3_callback

            view.add_item(button)
            view.add_item(button2)
            view.add_item(button3)
            await ctx.send(embed=embed, view=view)


async def setup(bot):
    await bot.add_cog(Level(bot))