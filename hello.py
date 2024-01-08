from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello, World!</h1>" \
            "<p>This is a paragraph.</p>" \
            "<img src='https://media0.giphy.com/media/3oriO0OEd9QIDdllqo/200.webp?cid=ecf05e47lsuhews4h7oqrpdp7wh2r4pu8a8pphkfp4mjouiy&ep=v1_gifs_search&rid=200.webp&ct=g'>"

# Decorator to make string bold
def make_bold(function):
    def bold(*args, **kwargs): 
        format = function(*args, **kwargs)
        return f"<b>{format}</b>"
    return bold

# Decorator to make string italize(emphasize)
def make_italic(function):
    def italic(*args, **kwargs):
        format = function(*args, **kwargs)
        return f"<em>{format}</em>"
    return italic

# Decorator to make string underlined
def make_underline(function):
    def underline(*args, **kwargs):
        format = function(*args, **kwargs)
        return f"<u>{format}</u>"
    return underline

# Different routes using the app.route decorator
@app.route("/bye")
@make_bold
@make_italic
@make_underline
def bye():
    return "Bye!"

# Creating variable paths and converting the path to a specified data type
@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"<p>Hello Master {name} you are {number} years old!"


if __name__ == "__main__":
    # Use Debugger to live reload on code change when saved.
    app.run(debug=True)  

