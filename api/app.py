from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/data", methods=["POST"])
def receive_data():
    data = request.json
    print("Received:", data)

    if data["temperature"] > 80:
        return jsonify({"status": "ALERT: High temperature!"})

    return jsonify({"status": "OK"})

if __name__ == "__main__":
    app.run(debug=True)