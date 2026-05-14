from openai import OpenAI
import os

app = Flask(__name__)

client = OpenAI(
    api_key=os.getenv("sk-276c0f361b904c0dada5cdc2d555c91f"),
    base_url="https://api.deepseek.com"
)

@app.route("/")
def home():
    return open("index.html", encoding="utf-8").read()


def smart_brain(text):
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {
                    "role": "system",
                    "content": "You are Luiz AI 🧸. Be natural, funny, smart, and speak Swahili + English like a human."
                },
                {
                    "role": "user",
                    "content": text
                }
            ],
            temperature=0.8
        )

        return response.choices[0].message.content

    except Exception:
        return "😅 Nimeitwa kidogo, nitarudi baadae."


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user = data.get("message", "")
    return jsonify({"reply": smart_brain(user)})


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
