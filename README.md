# DetectLive_Robot
*一隻自製Discord機器人的秘密*

以Discord.py為基底

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

sudo apt install python3.11(待測試)

sudo pip install python-dotenv

sudo pip install discord.py

sudo pip install pygsheets

sudo pip install xmltodict

sudo pip install websockets

sudo pip install apscheduler

sudo pip install quart

sudo pip install discord_webhook

1. **使用sudo運作**
	1. 需使用sudo運作，以防止1024以下端口權限不足產生錯誤使socket報錯{ sudo nohup python3 main.py & }。
    2. 運作後續使用{ sudo sh -c 'echo -1000 > /proc/[pid]/oom_score_adj' }指令來禁止oom程序kill，利用{ cat /proc/[pid]/oom_score_adj }確認。
    3. +SetNgrokLocal http://[ip] 指令設定位址時須注意後面不能有"反斜線"。

2. **使用screen運作**
    1. screen -S mysession 創建一個screen對話名稱為mysession
    2. sudo python3 main.py 直接運行
    3. 按下 Ctrl+A 然後按下 D。這將會把您從當前 screen 會話中分離出來，並返回到您的原始終端，而 screen 會話會在後台繼續運行。
    4. screen -r mysession 重新連接會話
    5. screen -ls 查看所有會話

## Swap掛載分區:
```
# 檢查Swap狀態，如果沒有Swap就不會有任何輸出資料。使用檢查記憶體使用狀況的free也能看到Swap，如果沒有設置則會看到Swap那行顯示0。
sudo swapon --show
# 建立一塊保留空間
sudo fallocate -l 1G /swapfile

# 設置讀寫權限
sudo chmod 600 /swapfile

# 建立Swap空間
sudo mkswap /swapfile
# Setting up swapspace version 1, size = 1024 MiB (1073737728 bytes)
# no label, UUID=b3b91233-6a5b-44d3-9d13-d7c66285a166

#啟動Swap空間
sudo swapon /swapfile

sudo swapon --show
# NAME      TYPE  SIZE  USED PRIO
# /swapfile file 1024M 20.3M   -2

# 修改設定為10，立即生效，從0到100，數字越高越積極使用Swap。但可以降低，非必要不用使用Swap降低速度。
sudo sysctl vm.swappiness=10
```
https://klab.tw/2022/06/what-is-linux-swap-and-how-to-add-it/
---

## 其他:
ps aux | grep "python3 main.py" | grep -v grep

scp -i Discord_key.pem -r [路徑] azureuser@20.127.165.218:/home/discordRobot/

scp -i Discord_key.pem [路徑] azureuser@20.127.165.218:~/discordRobot/
