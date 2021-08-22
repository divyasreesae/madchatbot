from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
from flask import Flask, render_template, request, jsonify,url_for
from connect import getresult

app = Flask(__name__)
output = ""

@app.route("/")
def home():
    return render_template('index.html')
    
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    # userText = 'msg';request.form['msg']
    print(str(userText))
    res = getresult(str(userText))
    output = res
    return res

if __name__ == '__main__':
   app.run()
   

