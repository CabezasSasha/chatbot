from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

chatbot = ChatBot('MyBot')

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

@app.route("/")
def home():
    return render_template("Chatbot.html")

@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    bot_response = str(chatbot.get_response(user_text))
    return bot_response

if __name__ == "__main__":
    app.run()
