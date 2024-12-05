from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

first_request = True
# Database configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db" # This is the database file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False          # This is to avoid a warning message
db = SQLAlchemy(app) # This is the database object

# User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80), nullable = False) 
    
@app.before_request # This method is executed before the first request
def create_tables():
    global first_request
    if first_request:
        first_request = False
        db.create_all()

@app.route("/add_user/<name>")
def add_user(name):
    user = User(name = name)
    db.session.add(user)
    db.session.commit() # This is to save the changes in the database
    return f"User {name} added successfully!"

#Route to obtain all users
@app.route("/get_users", methods = ["GET"])
def get_users():
    users = User.query.all()
    return jsonify([{"id": user.id, "name": user.name} for user in users])

# Route to obtain a user by id. 
@app.route("/get_user/<id>", methods = ["GET"])
def get_user(id):
    user = User.query.get(id)
    return jsonify({"id": user.id, "name": user.name})    

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

'''
To test the post and get methods, we have to use the following curl command:

GET: curl -X GET http://127.0.0.1:5000/api/data 

POST: curl -X POST http://127.0.0.1:5000/api/submit \
     -H "Content-Type: application/json" \
     -d '{"name": "Bob"}'

Where: -d is the data to be sent in the request and -H specifies the content type of the request.
'''