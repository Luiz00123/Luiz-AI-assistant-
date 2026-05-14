from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

@app.route("/")
def home():
    return "Luiz AI 🧸 is running!"

def brain(text):
    try:
        res = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are Luiz AI 🧸 funny Swahili-English assistant."},
                {"role": "user", "content": text}
            ]
        )
        return res.choices[0].message.content
    except Exception as e:
        return "😅 nimeitwa kidogo, kwaheri"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    msg = data.get("message", "")
    return jsonify({"reply": brain(msg)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
