from discord.ext import commands
from Function import SheetFn
from Global import globals

class CheckMemberData(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def CheckMemberData(self, ctx):
        print("開始執行確認伺服器成員資料...")
        await ctx.send("開始執行確認伺服器成員資料...")
        guild = ctx.guild
        members = guild.members
        for member in members:
            print(f"目前確認的member為 {member.name}，ID為 {member.id}")
            await ctx.send(f"目前確認的member為 {member.name}，ID為 {member.id}")
            if member.bot:
                pass
            else:
                # await ctx.send(globals.DetectLiveMemberData.get(member.id) is None)

                if globals.DetectLiveMemberData.get(str(member.id)) is None:
                    await ctx.send(f"- {member.name} 不存在於資料中，新增 {member.name} 於資料中... ")
                    SheetFn.SheetFunction.AddNewMemberData2Globals(member.id)
                    # await ctx.send(f"- 新增 {member.name} 於資料中... ")
                    # for data in globals.DetectLiveMemberData[1:]:
                    #     print(f"目前的資料為 {data}")
                    #     if(member.id == data[0]):
                    #         continue
                    #     else:
                    #         print(f"加入 {member.id} 的資料至DataBase...")
                    #         SheetFn.AddNewMemberDataFromGlobals(member.id)
                else:
                    await ctx.send(f"- {member.name} 已存在於資料中... ")

        # print(globals.DetectLiveMemberData)
        await SheetFn.SheetFunction.SetMemberData2Sheet()

async def setup(bot):
    await bot.add_cog(CheckMemberData(bot))