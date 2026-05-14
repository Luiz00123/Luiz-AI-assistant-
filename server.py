from flask import Flask, request, jsonify
from openai import OpenAI
import os

app = Flask(__name__)

# DeepSeek / OpenAI compatible client
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

@app.route("/")
def home():
    return open("index.html", encoding="utf-8").read()


def smart_brain(user_text):

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are Luiz AI 🧸. "
                        "You are a friendly, funny, intelligent assistant. "
                        "You speak natural Swahili and English like a real human. "
                        "Avoid repeating user input. Always respond naturally, short or medium length. "
                        "You can joke, explain, and help with coding or daily questions."
                    )
                },
                {
                    "role": "user",
                    "content": user_text
                }
            ],
            temperature=0.9
        )

        return response.choices[0].message.content

    except Exception as e:
        return "😅 Nimepata error kidogo, jaribu tena baadaye."


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user = data.get("message", "")

    reply = smart_brain(user)

    return jsonify({"reply": reply})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
