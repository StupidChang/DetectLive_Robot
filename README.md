# DetectLive_Robot
*一隻自製Discord機器人的秘密*

---
:::info
  ## 基本使用:
  main.py為DiscordRobot Kernel
  Cogs為放置Commands與Events
  Global裡的global.py放置全域變數
  Function裡SheetFn.py放置固定Function
:::

:::warning
## 使用注意:
1. 需使用sudo運作，以防止1024以下端口權限不足產生錯誤使socket報錯。
2. 運作後續使用{ sudo sh -c 'echo -1000 > /proc/[pid]/oom_score_adj' }指令來禁止oom程序kill。
3. +SetNgrokLocal http://52.186.179.207 指令設定位址時須注意後面不能有"反斜線"。
:::

