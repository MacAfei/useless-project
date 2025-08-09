from flask import Flask, request, jsonify, render_template
from leaderboard import add_click, get_leaderboard
from config import PORT

app = Flask(__name__)

@app.route("/click", methods=["POST"])
def click():
    data = request.json
    add_click(data["user"])
    return jsonify({"status": "ok"})

@app.route("/leaderboard", methods=["GET"])
def leaderboard_api():
    return jsonify(get_leaderboard())

@app.route("/")
def leaderboard_html():
    return render_template("leaderboard.html", leaderboard=get_leaderboard())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
