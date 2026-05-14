from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return open("index.html").read()

@app.route("/chat", methods=["POST"])
def chat():
    user = request.json["message"]

    # SIMPLE AI BRAIN (NO OPENAI = NO ERRORS)
    reply = smart_brain

def smart_brain(text):
    text = text.lower()

    if "hello" in text or "hi" in text:
        return "👋 Hey! Mimi ni Luiz 🧸 niko live sasa!"
    elif "how are you" in text:
        return "😊 Niko fresh kabisa, niko Render live!"
    elif "name" in text:
        return "🤖 Mimi ni Luiz AI 🧸"
    elif "love" in text:
        return "💙 Nimeundwa kuwa rafiki yako Luiz Vad"
    elif "bye" in text:
        return "👋 Tutaonana tena!"
    else:
        return f"🧠 Nimepokea: {text} (Luiz bado naendelea kujifunza)"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
def smart_brain(text):
    text = text.lower()

    if "hello" in text or "hi" in text:
        return "👋 Hey! Mimi ni Luiz 🧸 niko live!"
    elif "how are you" in text:
        return "😊 Niko fresh kabisa!"
    elif "name" in text:
        return "🤖 Mimi ni Luiz AI 🧸"
    elif "love" in text:
        return "💙 Nimeundwa kuwa rafiki yako Luiz Vad"
    elif "bye" in text:
        return "👋 Tutaonana!"
    else:
        return f"🧠 Nimepokea: {text}"
