from discord.ext import commands
import discord
import datetime
from Global import globals
from Function import SheetFn

class Shop(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['shop'])
    async def Shop(self, ctx, *args):
        embed = discord.Embed(
            title=f"DetectLive粉絲商店",
            # description=f"123456",
            color=0xff1acd
        )

        embed.set_author(name="DetectLive助手伯伯", icon_url='https://media.discordapp.net/attachments/1087810566342578198/1121099154077274204/logo-04.png?width=910&height=910')
        embed.add_field(name="🪙 [物品販賣項目]:", value=f"```神聖藥水x1```", inline=True)
        embed.set_footer(text='[=- DetectLive所屬製作 -=]', icon_url='https://media.discordapp.net/attachments/1087810566342578198/1121099154077274204/logo-04.png?width=910&height=910')

        embed.timestamp = datetime.datetime.now()

        view = discord.ui.View()

        button = discord.ui.Button(
            emoji="💰",
            label="DetectLive商店",
            style=discord.ButtonStyle.green
        )
        async def button_callback(interaction: discord.Interaction):
            if interaction.user.id == ctx.message.author.id:
                await interaction.response.defer()
                channel = interaction.channel

                message = f"[系統訊息] - {interaction.user.name} 打開了勇者商店!"
                await channel.send(message)
            else:
                await interaction.response.send_message("[系統訊息] - 您無權點擊此按鈕！", ephemeral=True)
        button.callback = button_callback

        button1 = discord.ui.Button(
            emoji="💰",
            label="DetectLive銀幣商店",
            style=discord.ButtonStyle.blurple
        )
        async def button1_callback(interaction: discord.Interaction):
            if interaction.user.id == ctx.message.author.id:
                await interaction.response.defer()
                channel = interaction.channel

                message = f"[系統訊息] - {interaction.user.name} 打開了勇者商店!"
                await channel.send(message)
            else:
                await interaction.response.send_message("[系統訊息] - 您無權點擊此按鈕！", ephemeral=True)
        button1.callback = button1_callback

        view.add_item(button)
        view.add_item(button1)
        await ctx.send(embed=embed, view=view)

async def setup(bot):
    await bot.add_cog(Shop(bot))