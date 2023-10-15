from discord.ext import commands
from Function import SheetFn
from discord.ext import commands, tasks
from Global import globals

class MessageHere(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def MessageHere(self, ctx):
        message = ("🔎 **竭誠歡迎您光臨DetectLive事務所，祝您在此度過美好的時光！** 🔍 \n"
                    +"\n"
                    + "**閱畢後蓋押下方印章，即為同意遵守本所規範。💮**  \n"
                    +"\n"
                    + "> # 《事務所規範》 \n"
                    + "> ## 為了保障您的安全，請嚴格遵守以下規範。 \n"
                    + "> - 禁止騷擾、攻擊他人。 \n"
                    + "> - 禁止提及個人資料。 \n"
                    + "> - 禁止養豬。 \n"
                    + "> - 禁止標記他人。 \n"
                    + "> - 禁止傳播色情、血腥、暴力、詐欺、惡意驚嚇等內容。 \n"
                    + "> - 事務所僅張貼內部資訊，若有張貼需求請來信詢問。 \n"
                    +"\n"
                    + "> # 《二創規範》 \n"
                    + "> ## 可進行無營利行為之二次創作，欲營利請來信詢問官方許可。 \n"
                    + "> 發布時歡迎使用Hashtag。有使用Hashtag之創作，視為可將該作品使用於直播封面或社群發文使用。 \n"
                    + "> （會於使用時標註作者，可能含去背、裁切、濾鏡等加工，欲商品化會另行詢問授權） \n"
                    + "> 剪輯與精華創作請標示原影片來源，並請於直播結束後發布。 \n"
                    +"> \n"
                    + "> - 禁止使旗下成員感到不快的創作活動。 \n"
                    + "> - 禁止以明示或暗示偽稱官方，或令官方遭受誤解之創作。 \n"
                    + "> - 禁止用於支持特定個人、組織、事件、宗教等宣傳用途。 \n"
                    + "> - 禁止有損形象之創作，如：血腥、暴力、詐欺等違反善良風俗之負面創作。 \n"
                    +"> \n"
                    + "> 如經官方研判內容不合適，官方可能會要求您下架。 \n"
                    +"\n"
                    + "**DetectLive保留所有規範的最終修改權與決定權，由偵探助手們做出的裁定與處置不接受異議。**")
        
        message2 = ("**由此前往 ➤**\n"
                    + "\n"
                    + "⛩️ ➤ **卜祀的陰陽寮**\n"
                    + "🐑 ➤ **羊可的雲層農場**\n"
                    + "🦄 ➤ **哈托卡的邊境森林**\n"
                    + "🌊 ➤ **阿爾菲的湖畔**\n"
                    + "🚬 ➤ **煙羅的煙火大會**\n"
                    + "🍷 ➤ **艾絲的快樂新家**\n"
                    + "👻 ➤ **朱玄的裸體海灘**\n"
                    + "🔮 ➤ **塞西的快樂老家**\n"
                    + "🛠️ ➤ **魯尼的提爾海姆號**\n"
                    + "\n"
                    + "🔍 ➤ **領取全域地圖逛大街囉**ᕕ ( ᐛ ) ᕗ")
        
        await ctx.send(message2)
  

async def setup(bot):
    await bot.add_cog(MessageHere(bot)) 