from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/followers")
def followers():
    user_id = request.args.get("userid")
    if not user_id:
        return jsonify({"error": "Missing userid"}), 400

    url = f"https://users.roblox.com/v1/users/{user_id}/followers/count"
    r = requests.get(url)
    data = r.json()
    count = data.get("count", 0)

    return jsonify({"followers": count})

if __name__ == "__main__":
    import os
port = int(os.environ.get("PORT", 3000))
app.run(host="0.0.0.0", port=port)

