import os
from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route("/")
def home():
    return open("index.html", encoding="utf-8").read()

@app.route("/chat", methods=["POST"])
def chat():
    user = request.json.get("message")

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are Luiz 🧸, a smart, friendly AI assistant. You respond naturally, not by repeating user text. Be helpful, short, and clear."
                },
                {"role": "user", "content": user}
            ]
        )

        reply = response.choices[0].message.content

    except Exception as e:
        reply = f"Error: {str(e)}"

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
