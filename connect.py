from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from flask import Flask, render_template, request, jsonify
from api_call import getUserData,get_credits,get_class_history
from py_linq import Enumerable

def getCredit(strg):
    data = getUserData()['users']
    user =Enumerable(data).where(lambda i:i['name'].find(strg.split()[0],0,len(i['name']))>0).first()
    ncredits = get_credits(user['id'])
    return ncredits

def getClassesHistory(strg):
    data = getUserData()['users']
    user =Enumerable(data).where(lambda i:i['name'].find(strg.split()[0],0,len(i['name']))>0).first()
    print(user['id'])
    nclasshistory = get_class_history(user['id'])
    return nclasshistory

def getresult(strg):
    bot = ChatBot("assistant")
    trainer = ListTrainer(bot)
    conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]
    trainer.train(conversation)
    try:
        trainer.train(['credit',strg.split()[0] +"has" + str(getCredit(strg))])
    except:
        print("Variable x is not defined")
    try:
        trainer.train(['class history',str(getClassesHistory(strg))])
    except:
        print("Variable x is not defined")

    response = bot.get_response(strg)
    
    return str(response)
    
