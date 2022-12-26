import os
import sys

from flask import Flask, jsonify, request, abort, send_file
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from fsm import TocMachine
from utils import send_text_message,send_button_message,send_image_message
from database import create, read, update, delete

load_dotenv()

machine = TocMachine(
    states=[
        "user",
        "weather", 
        "input_district", 
        "todo_list",
        "database_create",
        "database_create_input",
        "database_read",
        "database_update",        
        "database_update_inputNum",
        "database_update_inputState",
        "database_delete",
        "database_delete_input",
    ],
    transitions=[
        { "trigger": "advance","source": "user","dest": "weather","conditions": "is_going_to_weather"},
        {"trigger": "advance", "source": "weather","dest": "input_district", "conditions": "is_going_to_input_district"},
        {"trigger": "advance", "source":  "input_district","dest": "input_district", "conditions": "is_going_to_input_district"},

        # todo list
        {"trigger": "advance", "source": "user","dest": "todo_list", "conditions": "is_going_to_todo_list"},
        # create
        {"trigger": "advance", "source": "todo_list","dest": "database_create", "conditions": "is_going_to_database_create"},        
        {"trigger": "advance", "source": "database_create","dest": "database_create_input", "conditions": "is_going_to_database_create_input"},
         {"trigger": "advance", "source": "database_create_input","dest": "todo_list", "conditions": "is_going_to_todo_list"},
        # read
        {"trigger": "advance", "source": "todo_list","dest": "database_read", "conditions": "is_going_to_database_read"},        
        {"trigger": "advance", "source": "database_read","dest": "todo_list", "conditions": "is_going_to_todo_list"},  
        # update
        {"trigger": "advance", "source": "todo_list","dest": "database_update", "conditions": "is_going_to_database_update"},
        {"trigger": "advance", "source": "database_update","dest": "database_update_inputNum", "conditions": "is_going_to_database_update_inputNum"},       
        {"trigger": "advance", "source": "database_update_inputNum","dest": "database_update_inputState", "conditions": "is_going_to_database_update_inputState"}, 
        {"trigger": "advance", "source": "database_update_inputState","dest": "todo_list", "conditions": "is_going_to_todo_list"}, 
        # delete
        {"trigger": "advance", "source": "todo_list","dest": "database_delete", "conditions": "is_going_to_database_delete"},
        {"trigger": "advance", "source": "database_delete","dest": "database_delete_input", "conditions": "is_going_to_database_delete_input"},
        {"trigger": "advance", "source": "database_delete_input","dest": "todo_list", "conditions":"is_going_to_todo_list"},
        

        {"trigger": "go_back", 
            "source": [
                "weather", 
                "input_district", 
                "todo_list",
                "database_create",
                "database_create_input",                
                "database_read",
                "database_update",        
                "database_update_inputNum",
                "database_update_inputState",
                "database_delete",
                "database_delete_input",

            ],
            "dest": "user"
        },
    ],
    initial="user",
    auto_transitions=False,
    show_conditions=True,
)


app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv("LINE_CHANNEL_SECRET", None)
channel_access_token = os.getenv("LINE_CHANNEL_ACCESS_TOKEN", None)
if channel_secret is None:
    print("Specify LINE_CHANNEL_SECRET as environment variable.")
    sys.exit(1)
if channel_access_token is None:
    print("Specify LINE_CHANNEL_ACCESS_TOKEN as environment variable.")
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
parser = WebhookParser(channel_secret)
mode = 0

def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")

@app.route("/webhook", methods=["POST"])
def webhook_handler():
    signature = request.headers["X-Line-Signature"]
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info(f"Request body: {body}")

    # parse webhook body
    try:
        events = parser.parse(body, signature)
    except InvalidSignatureError:
        abort(400)


    # if event is MessageEvent and message is TextMessage, then echo text
    for event in events:
        if not isinstance(event, MessageEvent):
            continue
        if not isinstance(event.message, TextMessage):
            continue
        if not isinstance(event.message.text, str):
            continue
        print(f"\n 1. FSM STATE: {machine.state}")
        response = machine.advance(event)
        print(f"\n 2. FSM STATE: {machine.state}")

        if response == False:
            if event.message.text.lower() == 'fsm':
                send_image_message(event.reply_token, "https://627a-140-116-107-43.jp.ngrok.io/show-fsm")
            elif machine.state != 'user' and event.message.text.lower() == 'restart':
                send_text_message(event.reply_token, '隨時輸入『restart』返回主頁面。\n隨時輸入『fsm』可以得到當下的狀態圖。')                
                machine.go_back()
                print(f"\n 3. FSM STATE: {machine.state}")     
            elif machine.state == 'input_district':
                send_text_message(event.reply_token,'你還想知道台灣哪個地區的天氣狀況?')
            elif machine.state == 'database_update':
                send_text_message(event.reply_token,'請輸入清單項目的編號?')
            elif machine.state == 'user':
                send_text_message(event.reply_token, '輸入『fsm』可以得到當下的狀態圖。\n輸入『天氣』可以得到當下的狀態圖。\n輸入『todolist』可以得到當下的狀態圖。\n')                  

    return "OK"

@app.route("/show-fsm", methods=["GET"])
def show_fsm():
    machine.get_graph().draw("fsm.png", prog="dot", format="png")
    return send_file("fsm.png", mimetype="image/png")

        
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
