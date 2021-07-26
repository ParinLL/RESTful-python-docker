from flask import Flask
import os

app = Flask(__name__)
PORT = os.getenv('PORT', '80')

@app.route('/')
def hello_world():
    return 'Flask Dockerized'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=PORT)