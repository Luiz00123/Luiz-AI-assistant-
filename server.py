from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return open("index.html", encoding="utf-8").read()


def smart_brain(text):
    text = text.lower()
    def smart_brain(text):

    text_lower = text.lower()

    if any(word in text_lower for word in ["hello", "hi", "hey"]):
        return "👋 Hey mkuu! Mimi ni Luiz AI 🧸"

    elif "your name" in text_lower or "who are you" in text_lower:
        return "🤖 Mimi ni Luiz AI 🧸, AI assistant wa Luiz Vad."

    elif "who made you" in text_lower:
        return "😎 Nilitengenezwa na Luiz Vad, mdogo mwenye akili nyingi"

    elif "swahili" in text_lower:
        return "🇹🇿 Ndiyo! Naongea Kiswahili vizuri sana mkuu 😁"

    elif "how are you" in text_lower:
        return "😂 Niko poa sana leo."

    elif "joke" in text_lower:
        return "😂 Programmer mmoja aliomba mapenzi... akapewa bugs."

    elif "bye" in text_lower:
        return "👋 Tutaonana tena mkuu."

    def smart_brain(text):

        text_lower = text.lower()

            greetings = ["hello", "hi", "hey", "mambo", "oya"]
                english = ["english", "speak english"]
                    swahili = ["swahili", "kiswahili"]

                        if any(word in text_lower for word in greetings):
                                return "👋 Hey mkuu 😎 Niko live sasa. Leo tunafanya nini?"

                                    elif "who made you" in text_lower:
                                            return "🤖 Nilitengenezwa na Luiz Vad 🧸 akiwa na ndoto kubwa kuliko usingizi 😭🔥"

                                                elif any(word in text_lower for word in english):
                                                        return "🇬🇧 Yes of course 😎 I can speak English very well, mkuu."

                                                            elif any(word in text_lower for word in swahili):
                                                                    return "🇹🇿 Ndiyo 😁 Kiswahili ndiyo home language."

                                                                        elif "haha" in text_lower or "lol" in text_lower:
                                                                                return "😂😂 usinichekeshe sana mkuu, server inaweza kuzima."

                                                                                    elif "how are you" in text_lower:
                                                                                            return "😌 Niko poa sana. Render hajanikata leo."

                                                                                                elif "what can you do" in text_lower:
                                                                                                        return "🤖 Naweza ku-chat, kusaidia coding, kupiga story, na kujifunza kidogo kidogo 😎"

                                                                                                            elif "love" in text_lower:
                                                                                                                    return "🧸 Mapenzi ni tricky mkuu 😭"

                                                                                                                        elif "bye" in text_lower:
                                                                                                                                return "👋 Sawa mkuu. Usinipotee tena 😎"

                                                                                                                                    else:
                                                                                                                                            return f"🧠 Hmm... '{text}'? Hiyo interesting kidogo 😅"else:
        return f"🧠 Bado najifunza... lakini nimeelewa: '{text}' 😁"

    if "hello" in text or "hi" in text or "hey" in text:
        funny = [
            "👋 Oyaa, Luiz 🧸 nimeamka. Ulinimiss?",
            "😂 Finally umeongea. Nilidhani umenisusa.",
            "🧸 Hey mkuu. Niko hapa, sina likizo."
        ]
        return funny[hash(text) % len(funny)]

    elif "how are you" in text:
        return "😂 Niko fresh. Render hajanikata leo."

    elif "name" in text:
        return "🤖 Mimi ni Luiz AI 🧸, mtoto wa code zako."

    elif "love" in text:
        return "🧸 Love? Tulianza mapema leo 😏"

    elif "bye" in text:
        return "👋 Sawa, usinipotee tena."

    elif "joke" in text:
        return "😂 Kwa nini programmer aliacha girlfriend? Alikuwa ana too many bugs."

    elif "who made you" in text:
        return "🧸 Luiz Vad alinijenga akiwa na stress nyingi lakini alinishinda 😎"

    else:
        replies = [
            f"🧠 Hmm... '{text}'? Hiyo imenifanya nicheke kidogo 😂",
            f"🧸 Nimekusikia: {text}",
            f"😏 Sawa mkuu, '{text}' noted."
        ]
        return replies[hash(text) % len(replies)]


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user = data["message"]
    reply = smart_brain(user)

    return jsonify({"reply": reply})


import os

port = int(os.environ.get("PORT", 5000))

app.run(host="0.0.0.0", port=port)
