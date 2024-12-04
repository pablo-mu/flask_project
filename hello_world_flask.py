from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/about")
def about():
    return "This is the About Page!"

#Dynamic Route 
@app.route("/user/<username>")
def user_profile(username):
    return f"Hello, {username}!"

# Returning an HTML
@app.route("/html")
def html_page():
    return """
    <html>
        <head><title>Flask Example</title></head>
        <body>
            <h1>Welcome to Flask!</h1>
            <p>This is an HTML response.</p>
        </body>
    </html>
    """

@app.route("/template/<name>")
def template(name):
    return render_template("index.html", title = "Flask App", name = name)

@app.route("/form", methods = ["GET"])
def form():
    return render_template("form.html")

@app.route("/submit", methods = ["POST"])
def submit():
    name = request.form.get("name")
    return f"Hello, {name}!"

if __name__ == "__main__":
    app.run(debug = True)

