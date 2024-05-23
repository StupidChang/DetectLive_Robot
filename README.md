# DetectLive_Robot
*一隻自製Discord機器人的秘密*

---

## 基本使用:
main.py is DiscordRobot Kernel, can load/unload Cogs Commands.
Cogs have Commands and Events.
Can use +Load to load Commands's Command.
Global have global.py, this file place any global variable. 
Function have SheetFn.py,place fixed Function.

## 使用注意:
進行Azure機器安裝時需:

sudo apt update

sudo apt install python3.9(待測試)

sudo pip install python-dotenv

sudo pip install discord.py

sudo pip install pygsheets

sudo pip install xmltodict

sudo pip install websockets

sudo pip install apscheduler

sudo pip install quart

sudo pip install discord_webhook

1. 需使用sudo運作，以防止1024以下端口權限不足產生錯誤使socket報錯{ (sudo nohup python3 main.py & }。
2. 運作後續使用{ sudo sh -c 'echo -1000 > /proc/[pid]/oom_score_adj' }指令來禁止oom程序kill，利用{ cat /proc/[pid]/oom_score_adj }確認。
3. +SetNgrokLocal http://[ip] 指令設定位址時須注意後面不能有"反斜線"。

## 其他:
ps aux | grep "python3 main.py" | grep -v grep

scp -i Discord_key.pem -r C:\Users碩\Desktop\vscode\discordRobot azureuser@20.127.165.218:/home/discordRobot/
scp -i Discord_key.pem C:/Users/碩/Desktop/vscode/discordRobot/main.py azureuser@20.127.165.218:~/discordRobot/
