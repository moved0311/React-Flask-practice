# server.py
from flask import Flask
from flask_cors import cross_origin
import time

app = Flask(__name__)

@app.route("/")
@cross_origin()
def index():
    return {"res":"this is root"} 

@app.route("/hello")
@cross_origin()
def hello():
    return {"res":"Hello World!!!"}

@app.route("/time")
@cross_origin()
def getCurrentTime():
    return {"time": time.time()}

@app.route("/word")
@cross_origin()
def getWord():
    return {"word": "firstWord"}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
