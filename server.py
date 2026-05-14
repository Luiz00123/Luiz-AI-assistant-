import os
from flask import Flask, request, jsonify
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

 HEAD
message = [
    {"role": "system", "content": "You are Luiz 🧸, a smart, funny AI assistant like ChatGPT. Do not repeat user input. Answer naturally."}
]
0f20b62 (upgrade Luiz AI to ChatGPT brain)
@app.route("/")
def home():
    return open("index.html").read()

@app.route("/chat", methods=["POST"])
def chat():
    user = request.json["message"]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
<<<<<<< HEAD
        messages=messages + [{"role": "user", "content": user}]
    )

    ai = response.choices[0].message.content

    return jsonify({"reply": ai})
=======
        messages=[
            {"role": "system", "content": "You are Luiz 🧸, a smart AI assistant. Be clear and helpful."},
            {"role": "user", "content": user}
        ]
    )

    return jsonify({"reply": response.choices[0].message.content})
>>>>>>> 0f20b62 (upgrade Luiz AI to ChatGPT brain)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
