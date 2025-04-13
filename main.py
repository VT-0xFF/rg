from flask import Flask, request, jsonify

app = Flask(__name__)

developer_map = {
    "4663805453": "default",
    "1257293415": "DevCh"
}

@app.route("/log", methods=["POST"])
def log():
    data = request.get_json()
    return "OK"

@app.route("/alwaystrue", methods=["GET"])
def alwaystrue():
    return "true"

@app.route("/isdev", methods=["POST"])
def isdev():
    data = request.get_json()
    userid = data.get("userid", "")
    return developer_map.get(userid, "")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
