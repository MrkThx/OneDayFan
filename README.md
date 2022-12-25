# LineBot_OneDayFan
###
## 使用說明
#### 1.輸入"hi"以喚醒機器人
<img src="https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/320994692_876250613798966_6151682578256277136_n.jpg?_nc_cat=110&ccb=1-7&_nc_sid=ae9488&_nc_ohc=_h4cs4sJUUkAX8yf-Vm&_nc_ht=scontent-tpe1-1.xx&oh=03_AdRMhBNU3TIW_elpeZGxS8S56fOtTfEHPzGcGKfm5Y6tBA&oe=63CFB0CA" alt="Cover" width="30%"/>

#### 2 主選單中可選擇，"隊伍"，"比分"，"排名"
#### 隊伍：
輸入隊伍名(縮寫)
可選擇查看 "陣容名單"，"逐場比分"
* 陣容:
<img src="https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/321734336_2430525113754418_2625582927590412170_n.jpg?_nc_cat=101&ccb=1-7&_nc_sid=ae9488&_nc_ohc=2SxH5SBwteIAX_JHyO_&_nc_oc=AQnNgRiZTzG6fZutGUcLXwXqvoZT-oGDKyRxH63xF_ytuWsYQOqeukSCu_3i7z9Y7io&_nc_ht=scontent-tpe1-1.xx&oh=03_AdRGRyZqZ0KHkZf_DYs7sutBvBk5UpW1UzNmYRGH99yFdA&oe=63CFCCB1" alt="Cover" width="30%"/>

* 逐場比分:
<img src="https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/321850087_1249875659076866_4367365569423847876_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=ae9488&_nc_ohc=HQ5vf1VUVo8AX_UoTcR&_nc_ht=scontent-tpe1-1.xx&oh=03_AdSa_rJ0UYJI08CCS5-Ai5FREsxSc08onYUDuNOw3Vo6KQ&oe=63CFC3C4" alt="Cover" width="30%"/>

* 輸入"back"返回上一頁:
#### 比分:
可查看"冠軍賽"，"四強賽"，"八強賽"，"十六強"的比分

<img src="https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/320922993_558596585806449_7282815914449366251_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=ae9488&_nc_ohc=uwlkGgN2IHAAX-9DJHs&_nc_ht=scontent-tpe1-1.xx&oh=03_AdQWCLQX5UF2hbKtc9s3L9HMriKHehQesNVJ2Pxknx-gsg&oe=63CFDEC7" alt="Cover" width="30%"/>

#### 排名:
可查看前8名隊伍的排名和戰績

<img src="https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/320892911_847930139760559_1732440662870150267_n.jpg?_nc_cat=106&ccb=1-7&_nc_sid=ae9488&_nc_ohc=GVFQJMtwcuMAX9VSpPH&_nc_ht=scontent-tpe1-1.xx&oh=03_AdR-oVdCL03M10MgKHR8sdc4kCHs2hAYHco7p-JjbdOwJw&oe=63CFDA6F" alt="Cover" width="30%"/>

* 在任一狀態輸入"bye"會讓機器人回到初始狀態
## FSM:
* `user`初始狀態
* `score`主選單
* `games`使用者選擇比賽的輪次
  * `game_score`顯示比分，並重新讓使用者選擇輪次
* `team_list`使用者可輸入球隊縮寫
* `team`顯示球隊選單，包括比分和陣容(可輸入球隊為16強之球隊)
  * `team_games`顯示球隊比分
  * `team_roster`顯示球隊陣容(僅有4強球隊)
* `ranking`顯示8強球隊戰績和排名
* `endstate`結束狀態，回自動回到初始狀態
![GITHUB](https://i.imgur.com/q9EhvLm.png)
