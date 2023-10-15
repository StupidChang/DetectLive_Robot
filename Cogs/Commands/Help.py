from discord.ext import commands
import discord
import datetime

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def 管管使用教學(self, ctx, *args):
        message = ("```markdown\n"
                   + "#核心指令:\n"
                   + "└ +Load\n   ╙ 載入檔案。\n"
                   + "└ +unLoad\n   ╙ 卸載檔案。\n"
                   + "└ +reLoad\n   ╙ 重載檔案。\n"
                   + "└ +CheckCogs\n   ╙ 確認預設載入檔案。\n"
                   + "\n#表情相關:\n"
                   + "└ +SetReactionRole\n   ╙ 設定表情領取身分組 [+SetSetReactionRole 訊息ID 表情名稱 身分組ID]。\n"
                   + "└ +DeleteReactionRole\n   ╙ 刪除表情領取身分組 [+DeleteReactionRole 訊息ID 表情名稱 身分組ID]。\n"
                   + "\n#稱號相關:\n"
                   + "└ +Title New\n   ╙ 新增一個新稱號 [+Title New 表情 稱號 稱號的註解]。\n"
                   + "└ +Title Send\n   ╙ 發送稱號給使用者領取 [+Title Send 表情編號 (可領取時間)]，領取時間為分鐘，如無設定預設為30分鐘。\n"
                   + "└ +Title List\n   ╙ 顯示目前稱號列表。\n"
                   + "\n#資料卡相關:\n"
                   + "└ +Rank\n   ╙ 顯示DetectLive資料卡。\n"
                   + "└ +Rank title\n   ╙ 選擇DetectLive資料卡上之顯示稱號。\n"
                   + "└ +Rank set\n   ╙ 設定DetectLive資料卡自介。\n"
                   + "\n#伺服器資料相關:\n"
                   + "└ +CheckMemberData\n   ╙ 伺服器使用者資料遺失於資料庫中，利用此指令新增至資料庫。\n"
                   + "└ +SetWelcomeMessage(暫時無用)\n   ╙ 設定伺服器歡迎訊息，請利用\\n換行 [+SetWelcomeMessage 訊息]。\n"
                   + "└ +RequireSettingData\n   ╙ 重新請求資料庫資料至程式，手動修改資料後須重新請求，如Tag頻道、直播主資料等。\n"
                   + "└ +SaveData\n   ╙ 成員資料每六小時儲存一次，此指令手動執行儲存成員相關資料。\n"
                   + "└ +SetStreamerData\n   ╙ 新增一筆直播主資料至資料表中。\n"
                   + "└ +YoutubeSub\n   ╙ 新增直播主資料後請使用此指令向Youtube註冊。\n"
                   + "└ +TwitchSub\n   ╙ 新增直播主資料後請使用此指令向Twitch註冊。\n"
                   + "\n#特殊用途:\n"
                   + "└ +AddExperience\n   ╙ 增加自己的經驗值至1000。\n"
                   + "└ +GetChannelID\n   ╙ 輸入某個頻道的影片ID後返回頻道的Youtube ID\n"
                   + "└ +開始運作\n   ╙ 開啟機器人後，必須使用此指令執行 開啟伺服器、啟動備份、向Twitch註冊直播主、向Youtube註冊直播主。```")
        await ctx.send(message)

async def setup(bot):
    await bot.add_cog(Help(bot))