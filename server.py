from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

@app.route("/")
def home():
    return "Luiz AI 🧸 is running!"

def brain(text):
    try:
        res = client.chat.completions.create(
            model="gpt-3.5-turbo",
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
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
