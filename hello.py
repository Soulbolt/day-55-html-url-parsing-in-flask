from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello World!</p>"

@app.route("/bye")
def bye():
    return "<p>Bye!</p>"

@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"<p>Hello Master {name} you are {number} years old!"


if __name__ == "__main__":
    app.run(debug=True)  # Use Debugger to live reload on code change when saved.
