from discord.ext import commands
import discord
import datetime

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def 使用教學(self, ctx, *args):
        embed = discord.Embed(
            title="指令列表",
            url="https://realdrewdata.medium.com/",
            # description= "指令使用",
            color=0x5bbcff
        )
        embed.add_field(name="[ SetReactionRole ]:", value="設定表情領取身分組\n+SetSetReactionRole 訊息ID 表情名稱 身分組ID", inline=False)
        embed.add_field(name="[ DeleteReactionRole ]:", value="刪除表情領取身分組\n+DeleteReactionRole 訊息ID 表情名稱 身分組ID", inline=False)
        embed.add_field(name="[ CheckMemberData ]:", value="伺服器使用者資料遺失於資料庫中，利用此指令新增至資料庫", inline=False)
        embed.add_field(name="[ SetWelcomeMessage ]:", value="設定伺服器歡迎訊息\n+SetWelcomeMessage 訊息", inline=False)
        embed.add_field(name="[ RequireData ]:", value="重新請求資料庫資料至程式，手動修改資料後須重新請求，如Tag頻道、直播主資料等", inline=False)
        #setting footer
        embed.set_footer(text="身分組教學")
        #setting image
        embed.set_image(url="https://img.moegirl.org.cn/common/d/db/BA_Noa_ML.png")
        #setting thumbnail
        embed.set_thumbnail(url="https://img.moegirl.org.cn/common/d/db/BA_Noa_ML.png")
        #Setting timestamp
        embed.timestamp = datetime.datetime.now()
        #adding fields
        # await ctx.send(embed=embed)
        await ctx.send("'''這是一個測試檔案'''")

async def setup(bot):
    await bot.add_cog(Help(bot))