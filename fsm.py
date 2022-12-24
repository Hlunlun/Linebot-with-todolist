from transitions.extensions import GraphMachine

from utils import send_text_message,send_button_message,send_image_message
from bs4 import BeautifulSoup
import requests
from linebot.models import ImageCarouselColumn, URITemplateAction, MessageTemplateAction
import json
import numpy
import pandas as pd

city_choose = ['臺北市', '新北市','桃園市','臺中市', '臺南市', '高雄市', '新竹縣', '苗栗縣', '彰化縣', '南投縣', '雲林縣', '嘉義縣', '屏東縣', '宜蘭縣', '花蓮縣', '臺東縣', '澎湖縣', '金門縣', '連江縣', '基隆市', '新竹市', '嘉義市']
CID = []
class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
    
    def is_going_to_weather(self, event):
        text = event.message.text
        return text == "天氣"
    def on_enter_weather(self, event):
        send_text_message(event.reply_token, '請輸入台灣的哪個地區?')

    def is_going_to_input_district(self, event):
        text = event.message.text

        text = text.replace('台', '臺')

        if text in city_choose:
            return True

        return False

    def on_enter_input_district(self, event):



        send_text_message(event.reply_token, '阿')



    