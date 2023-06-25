from discord.ext import commands
import discord
import datetime
from Global import globals
from Function import SheetFn
import asyncio

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
    async def Level(self, ctx, *args):
        if(len(args) > 0):
            if(args[0] == "set"):
                globals.DetectLiveMemberData[str(ctx.message.author.id)]['LevelMessage'] = args[1]

        embed = discord.Embed(
            title="DetectLive - 等級資料卡",
            description=f"介紹: \n{globals.DetectLiveMemberData[str(ctx.message.author.id)]['LevelMessage']}",
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
        embed.add_field(name="[加入伺服器日期]:", value=globals.DetectLiveMemberData[str(ctx.message.author.id)]['JoinServerDate'], inline=True)
        embed.add_field(name="[已連續簽到]:", value=f"{globals.DetectLiveMemberData[str(ctx.message.author.id)]['SignInDate']} 天", inline=True) 
        embed.add_field(name="[目前等級]:", value=globals.DetectLiveMemberData[str(ctx.message.author.id)]['Level'], inline=False)
        embed.add_field(name="[距離下一等級‒經驗]:", value=progressbar, inline=True) #globals.DetectLiveMemberData[str(ctx.message.author.id)]['Exp']
        embed.add_field(name="[稱號]:", value="會飛的火龍", inline=False)
        embed.set_footer(text='[=- DetectLive所屬製作 -=]')
        embed.set_thumbnail(url="https://img.moegirl.org.cn/common/d/db/BA_Noa_ML.png")
        embed.timestamp = datetime.datetime.now()

        # print(globals.DetectLiveMemberData[str(ctx.message.author.id)])
        # print(globals.DetectLiveMemberData[str(ctx.message.author.id)]['Signln'])

        view = discord.ui.View()
        ModalView = discord.ui.View()

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

                    SheetFn.AddExp(str(ctx.message.author.id), 100)

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