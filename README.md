###### tags: `Line Bot` `FSM` `Python`
# Line Bot - 日常瑣事linebot (Implement FSM)
[example code](https://github.com/NCKU-CCS/TOC-Project-2020), [Hlunlun](https://github.com/Hlunlun/linebot/tree/master)

## 前言
1. 外出看天氣可以直接查詢
2. 也可以是todo list，隨時查看還有哪些事沒完成

## 環境：
python 3.9.13

## 技術
- pymogo : 連接資料庫
- api : 搜尋氣象資料
- mongodb : 存todolist

## How to start
1. `pip3 install pipenv`
2. 創一個 `.env` 檔包含
    - LINE_CHANNEL_SECRET
    - LINE_CHANNEL_ACCESS_TOKEN
    - WEATHER_API : 到[這裡](https://opendata.cwb.gov.tw/index)申請api
    - CONNECTION_STRING : 到[這裡](https://www.mongodb.com/cloud/atlas/lp/try4?utm_source=google&utm_campaign=search_gs_pl_evergreen_atlas_core_prosp-brand_gic-null_apac-tw_ps-all_desktop_eng_lead&utm_term=mongodb&utm_medium=cpc_paid_search&utm_ad=e&utm_ad_campaign_id=12212624371&adgroup=115749712503&gclid=CjwKCAiAhqCdBhB0EiwAH8M_GqHmbl1XW6yHgbzP4VmuBLvUhBQH6yFpdqSkwjKZ6l1pbos3pBctjRoCxngQAvD_BwE)創建mongodb帳號
3. pygraphviz : for windows
    - [how to install :movie_camera:](https://www.youtube.com/watch?v=XnxIfoUQeWw&list=PLxrVsqcpsInEp-4fEgT0F2nS9CXWCyKn6&index=1)
    - [Download graphviz](https://graphviz.org/download/)
4. open ngrok.exe : 記得先安裝
5. type `ngrok http 5000`
6. run app.py : `python app.py`

## 操作說明
- 基本操作  
    - `restart` : reset 回到初始狀態
    - `fsm` : 顯示狀態圖
- 架構
    - `weather` : 查詢天氣
    - `todo` : 可以對todolist做CRUD的編輯
- 使用示範
    - hello
        ![](https://user-images.githubusercontent.com/92961617/209499469-2b41ef0c-f0f1-4db5-bfe7-b0fe3540ec54.png)
    - 天氣 
        - 問地區
            ![](https://user-images.githubusercontent.com/92961617/209499562-e4d48dfb-94fb-44a0-84de-714305c7e6ae.png)
        - 可以繼續問，若是不想問了，就打`restart`
            ![](https://user-images.githubusercontent.com/92961617/209499717-98431050-c223-4df0-8ae3-3a63686fc073.png)
            ![](https://user-images.githubusercontent.com/92961617/209499732-beb564c8-f12c-41c4-970a-eedbed75e61e.png)
    - todolist
        - 問CRUD的哪個，一個項目進行完可以打todo就可以繼續下一個項目
           ![](https://user-images.githubusercontent.com/92961617/209499798-1bcf016d-a7ea-48eb-ada6-bfa377d31e0a.png)
        - Create
            ![](https://user-images.githubusercontent.com/92961617/209500637-181940da-fa30-47ee-9eb6-b915ec7c1a0a.png)
        - Read
            ![](https://user-images.githubusercontent.com/92961617/209501310-6ce5b010-6962-4955-8674-c5115f983b10.png)
        - Update
            - 輸入要更新的項目的編號
                ![](https://user-images.githubusercontent.com/92961617/209501523-c1a5086c-dd06-42b0-8573-75b67368a2c0.png)
            - 選擇要更新狀態
                ![](https://user-images.githubusercontent.com/92961617/209501578-7339004c-da6f-4306-9559-88d02e821ac1.png)
            - 最後顯示目前todolist
                ![](https://user-images.githubusercontent.com/92961617/209501643-18d0216c-b9f2-4894-abbc-36d437d4b930.png)
        - Delete
            - 輸入要刪除的項目的編號
                ![](https://user-images.githubusercontent.com/92961617/209501807-215e51e1-a639-470b-ab60-91eb70fefa9f.png)
            - 最後顯示目前todolist
                ![](https://user-images.githubusercontent.com/92961617/209501867-693cc6e6-0dc5-43e7-b5a3-b76fe3ab959d.png)
    - 輸入`fsm`
        ![](https://i.imgur.com/KH5QOun.png)

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

