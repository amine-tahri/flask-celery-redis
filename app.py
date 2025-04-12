from flask import Flask
from flask import current_app as app
app = Flask(__name__, static_url_path='/static')

@app.route("/")
def home():
    return "Hello, Flask!"

if __name__ == "__main__":
    app.run(debug=True)
