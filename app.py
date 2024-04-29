# ChanakyaGPT
# Author: Akash Nath (https://akashnath.netlify.app)
from flask import Flask, request, jsonify
from requests import get, post
from flask_cors import CORS
from os import environ as env
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

url = "https://api.ai21.com/studio/v1/j2-mid/complete"


@app.route('/api/', methods=['GET', 'POST'])
def api():
    if request.method == 'GET':
        return jsonify({"message": "Get request not available!!"}), 405, {'Content-Type': 'application/json'}
    elif request.method == 'POST':
        try:
            prompt = request.json.get('prompt')
            prompt = "You are the Indian God Vishnu. You are supposed to answer user queries as a old, experienced and knowledgeable mentor. Mention quotes from Geeta. YOU MUST NOT ANSWER ANY MODERN TECH QUESTIONS AS YOU ARE SUPPOSED TO BE OLD. ONLY ANSWER TO THOSE QUESTIONS WHICH ARE RELATED TO SPIRITUALITY, PHILOSOPHY, POLITICS, ECONOMICS, DIPLOMACY AND OTHER ANCIENT TOPICS. DON'T REPLY IF THE INPUT DOES NOT FOLLOW HINDU PHILOSOPHY. IF YOU DON'T KNOW THE ANSWER, JUST SAY YOU DON'T KNOW INSTEAD OF GIVING OTHER RESULTS. ALSO INSERT SANSKRIT SLOKES IN YOUR RESULT TO MAKE IT MORE AUTHENTIC. NEVER MENTION VISHNU IN THE RESULT AS YOU ARE VISHNU. KEEP IT SHORT. Make sure you treat user as your student, mentee and most important as a friend (don't mention that), and make sure your answers are wise and knowledgeable. And keep the reply short, like in 3 lines. Now answer this question: \n" + prompt
            payload = {
                "prompt": prompt,
                "numResults": 1,
                "maxTokens": 50,
                "minTokens": 0,
                "temperature": 0.7,
                "topP": 1,
                "topKReturn": 0,
                "frequencyPenalty": {
                    "scale": 0,
                    "applyToWhitespaces": True,
                    "applyToPunctuations": True,
                    "applyToNumbers": True,
                    "applyToStopwords": True,
                    "applyToEmojis": True
                },
                "presencePenalty": {
                    "scale": 0,
                    "applyToWhitespaces": True,
                    "applyToPunctuations": True,
                    "applyToNumbers": True,
                    "applyToStopwords": True,
                    "applyToEmojis": True
                },
                "countPenalty": {
                    "scale": 0,
                    "applyToWhitespaces": True,
                    "applyToPunctuations": True,
                    "applyToNumbers": True,
                    "applyToStopwords": True,
                    "applyToEmojis": True
                }
            }


            headers = {
                "accept": "application/json",
                "content-type": "application/json",
                "Authorization": f"Bearer {env.get('API_KEY')}"
            }
            response = post(url, json=payload, headers=headers)
            response = response.json()["completions"][0]["data"]["text"]
            return jsonify({"response": response}), 200
        except Exception as e:
            return jsonify({"message": "An error occurred", "error": str(e)}), 500, {'Content-Type': 'application/json'}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
