from flask import Flask, jsonify, request

app = Flask(__name__)

# This method returns a json response with static data
@app.route("/api/data", methods = ["GET"])
def get_data():
    data = {"name": "Alice", "city": "New York", "age": 25}
    return jsonify(data)

@app.route("/api/submit", methods = ["POST"])
def api_submit():
    json_data = request.json # Get the JSON data from the request
    name = json_data["name"]
    return jsonify({"message": f"Hello, {name}!"})

if __name__ == "__main__":
    app.run(debug = True)

