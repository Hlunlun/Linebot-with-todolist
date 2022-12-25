from transitions.extensions import GraphMachine
import os
from bs4 import BeautifulSoup
import requests
from linebot.models import ImageCarouselColumn, URITemplateAction, MessageTemplateAction
import json
import numpy
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

from utils import send_text_message,send_button_message,send_image_message
from database import create, read, update, delete

weather_api = os.getenv("WEATHER_API", None)

city_choose = ['臺北市', '新北市','桃園市','臺中市', '臺南市', '高雄市', '新竹縣', '苗栗縣', '彰化縣', '南投縣', '雲林縣', '嘉義縣', '屏東縣', '宜蘭縣', '花蓮縣', '臺東縣', '澎湖縣', '金門縣', '連江縣', '基隆市', '新竹市', '嘉義市']
# CID = ["63", "65", "68", "66", "67", "64", "10004", "10005", "10007", ""]
class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
    
    def is_going_to_weather(self, event):
        text = event.message.text
        return text == "天氣"
    def on_enter_weather(self, event):
        send_text_message(event.reply_token, '你想知道台灣哪個地區的天氣狀況?')

    def is_going_to_input_district(self, event):

        global district
        text = event.message.text

        text = text.replace('台', '臺')

        if text in city_choose:
            district = text
            return True

        return False

    def on_enter_input_district(self, event):
        url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001"
        params = {
            "Authorization": weather_api,
            "locationName": district,
        }
        response = requests.get(url, params=params)
        content = ''
        if response.status_code == 200:
            data = json.loads(response.text)

            location = data["records"]["location"][0]["locationName"]

            weather_elements = data["records"]["location"][0]["weatherElement"]
            start_time = weather_elements[0]["time"][0]["startTime"]
            end_time = weather_elements[0]["time"][0]["endTime"]
            weather_state = weather_elements[0]["time"][0]["parameter"]["parameterName"]
            rain_prob = weather_elements[1]["time"][0]["parameter"]["parameterName"]
            min_tem = weather_elements[2]["time"][0]["parameter"]["parameterName"]
            comfort = weather_elements[3]["time"][0]["parameter"]["parameterName"]
            max_tem = weather_elements[4]["time"][0]["parameter"]["parameterName"]

            content ='[' + location + ']' + ' 今明36小時天氣預報預報 \n'
            content += '起訖時間 : ' + str(start_time) + ' ~ '  + str(end_time) + '\n'
            content += '天氣概況 : ' + weather_state + '\n'
            content += '舒適程度 : ' + comfort + '\n'
            content += '最低溫度 : ' + min_tem + '\n'
            content += '最高溫度 : ' + max_tem + '\n'
            content += '降雨機率 : ' + rain_prob + '%' + ' (12小時分段)' + '\n'
        else:
            print("Can't get data!")

        send_text_message(event.reply_token,  content)

    def is_going_to_todo_list(self, event):
        text = event.message.text

        if 'todo' or 'todo list' or 'todolist' in text:
            return True

        return False
    def on_enter_todo_list(self, event):

        title = '請選擇你要如何編輯todo list'
        text = 'CRUD'
        btn = [
            MessageTemplateAction(
                label = 'Create',
                text ='Create'
            ),
            MessageTemplateAction(
                label = 'Read',
                text = 'Read'
            ),
            MessageTemplateAction(
                label = 'Update',
                text = 'Update'
            ),
            MessageTemplateAction(
                label = 'Delete',
                text = 'Delete',
            ),
        ]
        url = 'https://i.imgur.com/XkACYTI.jpeg'
        send_button_message(event.reply_token, title, text, btn, url)

    def is_going_to_input_crud(self, event):
        global crud
        text = event.message.text

        if text == 'Create' or text == 'Read' or text == 'Update' or text == 'Delete':
            crud = text
            return True

        return False     
        
    def on_enter_input_crud(self, event):

        if crud == 'Create':
            send_text_message(event.reply_token, '請輸入你的清單項目')
        elif crud == 'Read':
            send_text_message(event.reply_token, 
        send_text_message(event.reply_token, '這是你目前的todolist : \n'+read()) )
        elif crud == 'Update':
            send_text_message(event.reply_token, '你要更新todolist哪個項目的狀態?\n'+read())
        else:
            send_text_message(event.reply_token, '你要刪除todolist哪個項目?\n'+read())

    def is_going_to_database_create(self, event):
        if(crud != 'Create'):
            return False
        create(event.message.text)        
        return True

    def on_enter_database_create(self, event):

        send_text_message(event.reply_token, '這是你目前的todolist : \n'+read())

    def is_going_to_database_update(self, event):
        if(crud != 'Update' or event.message.text.isnumeric()==False):
            return False

        global todo_num 
        todo_num = int(event.message.text)
        return True

    def on_enter_database_update(self, event):

        title = '請選擇你要更新的狀態'
        text = ''
        btn = [
            MessageTemplateAction(
                label = 'todo',
                text ='todo'
            ),
            MessageTemplateAction(
                label = 'doing',
                text = 'doing',
            ),
            MessageTemplateAction(
                label = 'finished',
                text = 'finished',
            ),
        ]
        url = 'https://i.imgur.com/9inLzSB.png'
        send_button_message(event.reply_token, title, text, btn, url)
    
    def is_going_to_database_update_input(self, event):

        global todo_state
        text = event.message.text

        if text == 'todo' or text == 'doing' or text == 'finished':
            todo_state = text
            return True

        return False  

    def on_enter_database_update_input(self, event):
        update(todo_num, todo_state)
        send_text_message(event.reply_token, '這是你目前的todolist : \n'+read())
        

    def is_going_to_database_delete(self, event):
        if crud != 'Delete':
            return False

        delete(int(event.message.text))
        return True
        
    def on_enter_database_database_delete(self, event):
        
        send_text_message(event.reply_token, '這是你目前的todolist : \n'+read())


    