import os
from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

messages = [
    {"role": "system", "content": "You are Luiz 🧸, a smart, funny AI assistant like ChatGPT. Do not repeat user input. Answer naturally."}
]

@app.route("/")
def home():
    return open("index.html").read()

@app.route("/chat", methods=["POST"])
def chat():
    user = request.json["message"]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages + [{"role": "user", "content": user}]
    )

    ai = response.choices[0].message.content

    return jsonify({"reply": ai})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
