from flask import Flask, render_template, request, jsonify
from nltk.chat.util import Chat, reflections

app = Flask(__name__)
pairs = [
   ["hi|hello|hey|hola|yo", ["Hello!", "Hi there!", "Hey!"]],
   ["hi|hello|hey|hola|yo", ["Hello!", "Hi there!", "Hey!"]],
    ["how are you|how r u|how's it going", ["I'm just a bot, but thanks for asking!"]],
    ["what's up|what's new|how's it going", ["Not much, just here to chat with you!"]],
    ["help|assist|can you help me", ["Sure! What do you need help with?"]],
    ["what's your name|who are you", ["I'm a chatbot created to assist you."]],
    ["who created you|who made you|your creator", ["I was created by Harsha."]],
    ["what can you do|your abilities|what are you capable of", ["I can  chat with you, answer basic questions, and more!"]],
    ["tell me a joke|make me laugh|say something funny", ["Why don’t scientists trust atoms? Because they make up everything!"]],
    ["do you love me|love you|do u ❤️ me", ["I'm a bot, but I care about you! ❤️"]],
    ["weather|what is the weather|is it raining", ["I'm not connected to weather APIs yet."]],
    
    ["thank you|thanks|tq|ty|thx", ["You're welcome!", "No problem!", "Anytime!"]],
    ["bye|goodbye|see you|quit|exit", ["Goodbye!", "See you later!", "Bye!"]],
    ["how are you|how's it going|how r u", ["I'm fine, thank you!", "Doing well, how about you?"]],
    ["what is your name|who are you", ["I'm a chatbot created to assist you."]],
    ["who created you|your developer|who is your creator", ["My creator is Harsha."]],
    ["what can you do|your skills|what are you capable of", ["I can chat with you, answer basic questions, and more!"]],
    ["tell me a joke|make me laugh|say something funny", ["Why don’t scientists trust atoms? Because they make up everything!"]],
    ["do you love me|love you|do u ❤️ me", ["I'm a bot, but I care about you! ❤️"]],
    ["weather|what is the weather|is it raining", ["I'm not connected to weather APIs yet."]],
]


chatbot = Chat(pairs, reflections)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get("message")
    response = chatbot.respond(user_input)
    return jsonify({"response": response or "Sorry, I don't understand."})

if __name__ == '__main__':
    app.run(debug=True)
