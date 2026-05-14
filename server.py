from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return open("index.html").read()

@app.route("/chat", methods=["POST"])
def chat():
    user = request.json["message"]

    reply = f"Luiz 🧸: umeandika -> {user}"

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
