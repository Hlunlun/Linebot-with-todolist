import os
from dotenv import load_dotenv
from pymongo import MongoClient
import datetime
load_dotenv()

def get_current_time():
    current_time = datetime.datetime.now()
    time = str(current_time.year) + '/' + str(current_time.month) + '/' + str(current_time.day) + ' ' + str(current_time.hour) + ':' + str(current_time.minute)
    return time

def get_database():
    
    connection_string = os.getenv("CONNECTION_STRING", None)
    client = MongoClient(connection_string)
    db = client.todo
    return db

def create(todo):
    db = get_database()
    collection = db['list']
    num = collection.count_documents({})
    data = {
        'num' : num+1,
        'item' : todo,
        'time' : get_current_time(),
        'state' : 'todo'
    }
    collection.insert_one(data)

def read():
    db = get_database()
    collection = db['list']
    todo_list = collection.find({})
    results = ""
    for todo in todo_list:
        results += str(todo['num']) + '. ' + todo['item'] + ' : ' +  todo['state'] + '\n'
    
    return results

def update(num,state):
    db = get_database()
    collection = db['list']

    collection.update_one(
        {'num': {'$eq' : num}},
        {'$set':{
            'state' : state,
            'time' : get_current_time(),
        }}
    )


def delete(num):
    db = get_database()
    collection = db['list']
    todo_list = collection.find({})

    collection.delete_one({'num' : {'$eq' : num}})

    for todo in todo_list:
        if todo['num'] > num:
            collection.update_one({'item' : {'$eq' : todo['item']}},{'$set' : {'num' : todo['num']-1}})



if __name__ == "__main__": 
    db = get_database()
    collection = db['list']
    todo_list = collection.find({})
    # create('eat')
    # create('sleep')

    # delete(1)
    # print(read())
