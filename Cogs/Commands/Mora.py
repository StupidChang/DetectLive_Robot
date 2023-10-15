from discord.ext import commands
import discord
import random
from Function import SheetFn
from Global import globals
# class MyModal(discord.ui.Modal, title = "測試"):
#     answer = discord.ui.TextInput(label="HI", placeholder="請輸入簡介",style= discord.TextStyle.short)

#     async def on_submit(self, interaction: discord.Interaction):
#         embed = discord.Embed(title = self.title, description = f"{self.answer.label}**\n{self.answer}", timestamp = datetime.now(), color = discord.Colour.blue())
#         embed.set_author(name = interaction.user, icon_url=interaction.user.avatar)
#         await interaction.response.send_message(embed = embed)    

class Mora(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def 猜拳(self, ctx, *args):
            A = ["<:Niekou:1147091697180872755>SS級偵探助手", "⛩️陰陽寮的守門人", "🐑雲層牧場的管理員", "🦄邊境森林的小兔", "🌊湖畔的小魚", "🚬超大的老X", "🍷艾情公寓的守衛", "👻裸體海灘的參與者", "🔮異世界的快樂小孩"]
            choose = A[random.randint(0, 8)]
            B = f"**[{str(ctx.message.author)}]** 對 **[{choose}]** 發起了一場風起雲湧的剪刀石頭布戰鬥...⚔️\n請決定您的選擇吧!!"  

            view = discord.ui.View()
            view2 = discord.ui.View()

            button = discord.ui.Button(
                emoji="✌️",
                label="剪刀",
                style=discord.ButtonStyle.primary,
            )
            async def button_callback(interaction: discord.Interaction):
                    if interaction.user.id == ctx.message.author.id:
                        await interaction.response.defer()

                        channel = interaction.channel
                        if  int(random.randint(1,500)) < 490:
                            
                            response = random.choice(['剪刀', '石頭', '布'])
                            if response == "剪刀":
                                message = f"**[{choose}]** 對 **[{str(ctx.message.author)}]** 使出了 **[{response}]**，這局沒有勝負~"
                            elif response == "石頭":
                                message = f"**[{choose}]** 對 **[{str(ctx.message.author)}]** 使出了 **[{response}]**，這局您落敗了QQ"
                            elif response == "布":
                                globals.DetectLiveMemberData[str(interaction.user.id)]["MoraWinNumber"] += 1
                                if globals.DetectLiveMemberData[str(interaction.user.id)]["MoraWinNumber"] == 150:
                                    await SheetFn.SheetFunction.DirectUpdateMemberTitleNumber("16", interaction.user.id)
                                    message = f"**[{choose}]** 對 **[{str(ctx.message.author)}]** 使出了 **[{response}]**，這局是您贏拉~ \n[系統訊息] - **[{str(ctx.message.author)}]** 已獲得一個新稱號 - **[🕵️猜拳的堅強挑戰者]**"
                                else:
                                    message = f"**[{choose}]** 對 **[{str(ctx.message.author)}]** 使出了 **[{response}]**，這局是您贏拉~"

                            button.disabled = True
                            button2.disabled = True
                            button3.disabled = True
                            await interaction.message.edit(view=view)
                        else:
                            button.disabled = True
                            button2.disabled = True
                            button3.disabled = True
                            await interaction.message.edit(view=view)
                            message = f"您對 **[{choose}]** 使出了 布 ，但是 **[{choose}]** 突然逃跑了，要追上他嗎?"
                            Yes = discord.ui.Button(
                                emoji="⭕",
                                label="追上他",
                                style=discord.ButtonStyle.primary,
                                disabled=False
                            )
                            async def Yes_callback(interaction: discord.Interaction):
                                if interaction.user.id == ctx.message.author.id:
                                    await interaction.response.defer()
                                    channel = interaction.channel
                                    message = f"您選擇追上了 **[{choose}]** ，但是 **[{choose}]** 實在跑太快了，所以還是讓 **[{choose}]** 逃跑了。"

                                    Yes.disabled = True
                                    No.disabled = True
                                    What.disabled = True
                                    await interaction.message.edit(view=view2)

                                    await channel.send(message)
                                else:
                                    await interaction.response.send_message("[系統訊息] - 您無權點擊此按鈕！", ephemeral=True)
                            Yes.callback = Yes_callback

                            No = discord.ui.Button(
                                emoji="❌",
                                label="不追",
                                style=discord.ButtonStyle.primary,
                                disabled=False
                            )
                            async def No_callback(interaction: discord.Interaction):
                                if interaction.user.id == ctx.message.author.id:
                                    await interaction.response.defer()
                                    channel = interaction.channel
                                    message = f"您選擇不追了 **[{choose}]** ，但是 **[{choose}]** 就這樣跑掉了...。"

                                    Yes.disabled = True
                                    No.disabled = True
                                    What.disabled = True
                                    await interaction.message.edit(view=view2)

                                    await channel.send(message)
                                else:
                                    await interaction.response.send_message("[系統訊息] - 您無權點擊此按鈕！", ephemeral=True)
                            No.callback = No_callback

                            What = discord.ui.Button(
                                emoji="<:21:1095048057281843230>",
                                label="what??",
                                style=discord.ButtonStyle.primary,
                                disabled=False
                            )
                            async def What_callback(interaction: discord.Interaction):
                                if interaction.user.id == ctx.message.author.id:
                                    await interaction.response.defer()
                                    channel = interaction.channel
                                    message = f"因為實在太傻眼，所以不小心脫口而出:What??，結果 **[{choose}]** 覺得很有趣，於是他折回來並且賦予你一個響徹世界的頭銜... \n[系統訊息] - **[{str(ctx.message.author)}]** 已獲得一個新稱號 - **[👑剪刀石頭布大師✌️🖐️✊]**"
                                    await SheetFn.SheetFunction.DirectUpdateMemberTitleNumber("15", interaction.user.id)
                                    Yes.disabled = True
                                    No.disabled = True
                                    What.disabled = True
                                    await interaction.message.edit(view=view2)

                                    await channel.send(message)
                                else:
                                    await interaction.response.send_message("[系統訊息] - 您無權點擊此按鈕！", ephemeral=True)
                            What.callback = What_callback

                            view2.add_item(Yes)
                            view2.add_item(No)
                            view2.add_item(What)

                        await channel.send(message, view=view2)
                    else:
                        await interaction.response.send_message("[系統訊息] - 您無權點擊此按鈕！", ephemeral=True)
            button.callback = button_callback
            
            button2 = discord.ui.Button(
                emoji="✊",
                label="石頭",
                style=discord.ButtonStyle.primary,
            )
            async def button2_callback(interaction: discord.Interaction):
                    if interaction.user.id == ctx.message.author.id:
                        await interaction.response.defer()

                        channel = interaction.channel
                        if int(random.randint(1,500)) < 490:
                            response = random.choice(['剪刀', '石頭', '布'])
                            if response == "剪刀":
                                globals.DetectLiveMemberData[str(interaction.user.id)]["MoraWinNumber"] += 1
                                if globals.DetectLiveMemberData[str(interaction.user.id)]["MoraWinNumber"] == 150:
                                    await SheetFn.SheetFunction.DirectUpdateMemberTitleNumber("16", interaction.user.id)
                                    message = f"**[{choose}]** 對 **[{str(ctx.message.author)}]** 使出了 **[{response}]**，這局是您贏拉~ \n[系統訊息] - **[{str(ctx.message.author)}]** 已獲得一個新稱號 - **[🕵️猜拳的堅強挑戰者]**"
                                else:
                                    message = f"**[{choose}]** 對 **[{str(ctx.message.author)}]** 使出了 **[{response}]**，這局是您贏拉~"
                            elif response == "石頭":
                                message = f"**[{choose}]** 對 **[{str(ctx.message.author)}]** 使出了 **[{response}]**，這局沒有勝負~"
                            elif response == "布":
                                message = f"**[{choose}]** 對 **[{str(ctx.message.author)}]** 使出了 **[{response}]**，這局您落敗了QQ"

                            button.disabled = True
                            button2.disabled = True
                            button3.disabled = True
                            await interaction.message.edit(view=view)
                        else:
                            button.disabled = True
                            button2.disabled = True
                            button3.disabled = True
                            await interaction.message.edit(view=view)
                            message = f"您對 **[{choose}]** 使出了 布 ，但是 **[{choose}]** 突然逃跑了，要追上他嗎?"
                            Yes = discord.ui.Button(
                                emoji="⭕",
                                label="追上他",
                                style=discord.ButtonStyle.primary,
                                disabled=False
                            )
                            async def Yes_callback(interaction: discord.Interaction):
                                if interaction.user.id == ctx.message.author.id:
                                    await interaction.response.defer()
                                    channel = interaction.channel
                                    message = f"您選擇追上了 **[{choose}]** ，但是 **[{choose}]** 實在跑太快了，所以還是讓 **[{choose}]** 逃跑了。"

                                    Yes.disabled = True
                                    No.disabled = True
                                    What.disabled = True
                                    await interaction.message.edit(view=view2)

                                    await channel.send(message)
                                else:
                                    await interaction.response.send_message("[系統訊息] - 您無權點擊此按鈕！", ephemeral=True)
                            Yes.callback = Yes_callback

                            No = discord.ui.Button(
                                emoji="❌",
                                label="不追",
                                style=discord.ButtonStyle.primary,
                                disabled=False
                            )
                            async def No_callback(interaction: discord.Interaction):
                                if interaction.user.id == ctx.message.author.id:
                                    await interaction.response.defer()
                                    channel = interaction.channel
                                    message = f"您選擇不追了 **[{choose}]** ，但是 **[{choose}]** 就這樣跑掉了...。"

                                    Yes.disabled = True
                                    No.disabled = True
                                    What.disabled = True
                                    await interaction.message.edit(view=view2)

                                    await channel.send(message)
                                else:
                                    await interaction.response.send_message("[系統訊息] - 您無權點擊此按鈕！", ephemeral=True)
                            No.callback = No_callback

                            What = discord.ui.Button(
                                emoji="<:21:1095048057281843230>",
                                label="what??",
                                style=discord.ButtonStyle.primary,
                                disabled=False
                            )
                            async def What_callback(interaction: discord.Interaction):
                                if interaction.user.id == ctx.message.author.id:
                                    await interaction.response.defer()
                                    channel = interaction.channel
                                    message = f"因為實在太傻眼，所以不小心脫口而出:What??，結果 **[{choose}]** 覺得很有趣，於是他折回來並且賦予你一個響徹世界的頭銜... \n[系統訊息] - **[{str(ctx.message.author)}]** 已獲得一個新稱號 - **[👑剪刀石頭布大師✌️🖐️✊]**"
                                    await SheetFn.SheetFunction.DirectUpdateMemberTitleNumber("15", interaction.user.id)
                                    Yes.disabled = True
                                    No.disabled = True
                                    What.disabled = True
                                    await interaction.message.edit(view=view2)

                                    await channel.send(message)
                                else:
                                    await interaction.response.send_message("[系統訊息] - 您無權點擊此按鈕！", ephemeral=True)
                            What.callback = What_callback

                            view2.add_item(Yes)
                            view2.add_item(No)
                            view2.add_item(What)

                        await channel.send(message, view=view2)
                    else:
                        await interaction.response.send_message("[系統訊息] - 您無權點擊此按鈕！", ephemeral=True)
            button2.callback = button2_callback

            button3 = discord.ui.Button(
                emoji="🖐️",
                label="布",
                style=discord.ButtonStyle.primary,
            )
            async def button3_callback(interaction: discord.Interaction):
                    if interaction.user.id == ctx.message.author.id:
                        await interaction.response.defer()

                        channel = interaction.channel
                        if int(random.randint(1,500)) < 490:
                            response = random.choice(['剪刀', '石頭', '布'])
                            if response == "剪刀":
                                message = f"**[{choose}]** 對 **[{str(ctx.message.author)}]** 使出了 **[{response}]**，這局您落敗了QQ"
                            elif response == "石頭":
                                globals.DetectLiveMemberData[str(interaction.user.id)]["MoraWinNumber"] += 1
                                if globals.DetectLiveMemberData[str(interaction.user.id)]["MoraWinNumber"] == 150:
                                    await SheetFn.SheetFunction.DirectUpdateMemberTitleNumber("16", interaction.user.id)
                                    message = f"**[{choose}]** 對 **[{str(ctx.message.author)}]** 使出了 **[{response}]**，這局是您贏拉~ \n[系統訊息] - **[{str(ctx.message.author)}]** 已獲得一個新稱號 - **[🕵️猜拳的堅強挑戰者]**"
                                else:
                                    message = f"**[{choose}]** 對 **[{str(ctx.message.author)}]** 使出了 **[{response}]**，這局是您贏拉~"
                            elif response == "布":
                                message = f"**[{choose}]** 對 **[{str(ctx.message.author)}]** 使出了 **[{response}]**，這局沒有勝負~"

                            button.disabled = True
                            button2.disabled = True
                            button3.disabled = True
                            await interaction.message.edit(view=view)
                        else:
                            button.disabled = True
                            button2.disabled = True
                            button3.disabled = True
                            await interaction.message.edit(view=view)
                            message = f"您對 **[{choose}]** 使出了 布 ，但是 **[{choose}]** 突然逃跑了，要追上他嗎?"
                            Yes = discord.ui.Button(
                                emoji="⭕",
                                label="追上他",
                                style=discord.ButtonStyle.primary,
                                disabled=False
                            )
                            async def Yes_callback(interaction: discord.Interaction):
                                if interaction.user.id == ctx.message.author.id:
                                    await interaction.response.defer()
                                    channel = interaction.channel
                                    message = f"您選擇追上了 **[{choose}]** ，但是 **[{choose}]** 實在跑太快了，所以還是讓 **[{choose}]** 逃跑了。"

                                    Yes.disabled = True
                                    No.disabled = True
                                    What.disabled = True
                                    await interaction.message.edit(view=view2)

                                    await channel.send(message)
                                else:
                                    await interaction.response.send_message("[系統訊息] - 您無權點擊此按鈕！", ephemeral=True)
                            Yes.callback = Yes_callback

                            No = discord.ui.Button(
                                emoji="❌",
                                label="不追",
                                style=discord.ButtonStyle.primary,
                                disabled=False
                            )
                            async def No_callback(interaction: discord.Interaction):
                                if interaction.user.id == ctx.message.author.id:
                                    await interaction.response.defer()
                                    channel = interaction.channel
                                    message = f"您選擇不追了 **[{choose}]** ，但是 **[{choose}]** 就這樣跑掉了...。"

                                    Yes.disabled = True
                                    No.disabled = True
                                    What.disabled = True
                                    await interaction.message.edit(view=view2)

                                    await channel.send(message)
                                else:
                                    await interaction.response.send_message("[系統訊息] - 您無權點擊此按鈕！", ephemeral=True)
                            No.callback = No_callback

                            What = discord.ui.Button(
                                emoji="<:21:1095048057281843230>",
                                label="what??",
                                style=discord.ButtonStyle.primary,
                                disabled=False
                            )
                            async def What_callback(interaction: discord.Interaction):
                                if interaction.user.id == ctx.message.author.id:
                                    await interaction.response.defer()
                                    channel = interaction.channel
                                    message = f"因為實在太傻眼，所以不小心脫口而出:What??，結果 **[{choose}]** 覺得很有趣，於是他折回來並且賦予你一個響徹世界的頭銜... \n[系統訊息] - **[{str(ctx.message.author)}]** 已獲得一個新稱號 - **[👑剪刀石頭布大師✌️🖐️✊]**"
                                    await SheetFn.SheetFunction.DirectUpdateMemberTitleNumber("15", interaction.user.id)
                                    Yes.disabled = True
                                    No.disabled = True
                                    What.disabled = True
                                    await interaction.message.edit(view=view2)

                                    await channel.send(message)
                                else:
                                    await interaction.response.send_message("[系統訊息] - 您無權點擊此按鈕！", ephemeral=True)
                            What.callback = What_callback

                            view2.add_item(Yes)
                            view2.add_item(No)
                            view2.add_item(What)

                        await channel.send(message, view=view2)
                    else:
                        await interaction.response.send_message("[系統訊息] - 您無權點擊此按鈕！", ephemeral=True)
            button3.callback = button3_callback

            view.add_item(button)
            view.add_item(button2)
            view.add_item(button3)
            
            await ctx.send(B, view=view)

async def setup(bot):
    await bot.add_cog(Mora(bot))