# 日常瑣事 linebot

## 前言
1. 外出看天氣可以直接查詢
2. 也可以是todo list，隨時查看還有哪些事沒完成
3. 放假時，存了幾部最近看的電影，周末來看
4. 

## 環境：
python 3.9.13

## 技術
- pymogo : 連接資料庫
- Beautiful : 

## How to start
1. `pip3 install pipenv`
2. 創一個 `.env` 檔包含
    - LINE_CHANNEL_SECRET
    - LINE_CHANNEL_ACCESS_TOKEN
    - WEATHER_API : 到[這裡](https://opendata.cwb.gov.tw/index)申請api
    - CONNECTION_STRING : 到[這裡](https://www.mongodb.com/cloud/atlas/lp/try4?utm_source=google&utm_campaign=search_gs_pl_evergreen_atlas_core_prosp-brand_gic-null_apac-tw_ps-all_desktop_eng_lead&utm_term=mongodb&utm_medium=cpc_paid_search&utm_ad=e&utm_ad_campaign_id=12212624371&adgroup=115749712503&gclid=CjwKCAiAhqCdBhB0EiwAH8M_GqHmbl1XW6yHgbzP4VmuBLvUhBQH6yFpdqSkwjKZ6l1pbos3pBctjRoCxngQAvD_BwE)創建mongodb帳號
3. open ngrok.exe : 記得先安裝
4. type `ngrok http 5000`
5. run app.py : `python app.py`

## 操作說明
- 基本操作  
    - `restart` : reset 回到初始狀態
    - `fsm` : 顯示狀態圖
- 架構
    - `weather` : 查詢天氣
    - `todo` : 可以對todolist做CRUD的編輯
    - `movie` : 可以存喜歡看的電影


## 參考資料
- [sample code](https://github.com/NCKU-CCS/TOC-Project-2020/blob/master/app.py)
-  [ngrok](https://dashboard.ngrok.com/login)
-  [【Chatbot】(全圖文說明) ngrok 本地伺服器設定方法 – LINE bot local server](https://www.wongwonggoods.com/python/python_chatbot/linebot-local-server-ngork/)
-  [SiuYingCheng linebot_project](https://github.com/SiuYingCheng/linebot_project)
-  [爬取現在天氣](https://steam.oxxostudio.tw/category/python/spider/current-weather.html)
-  [氣象資料開放平台](https://opendata.cwb.gov.tw/index)
-  [[Python爬蟲教學]7個Python使用BeautifulSoup開發網頁爬蟲的實用技巧](https://www.learncodewithmike.com/2020/02/python-beautifulsoup-web-scraper.html)
-  [一般天氣預報-今明36小時天氣預報](https://opendata.cwb.gov.tw/dataset/forecast/F-C0032-001)
-  [Day 27：專案07 - 天氣小助理01 | 氣象資料API](https://ithelp.ithome.com.tw/articles/10276375)
### .gitignore
-  [How to ignore certain files in Git](https://stackoverflow.com/questions/4308610/how-to-ignore-certain-files-in-git)
### line develop
-  [line develop](https://account.line.biz/login?redirectUri=https%3A%2F%2Fdevelopers.line.biz%2Fconsole%2Fchannel%2F1657725664)



