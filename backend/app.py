from flask import Flask , request , jsonify


from dotenv import load_dotenv
import os

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

uri = os.getenv("MONGO_URI")

client = MongoClient(uri, server_api=ServerApi("1"))
db = client.users
collection = db["email_pass"]

app = Flask(__name__)


@app.route("/")
def hello():
    return "yo this is running!!!"

@app.route("/submit" , methods=["POST"])
def submit():

    data = request.json
    collection.insert_one(data)
    return jsonify({
        "message": "Data Submitted Successfully"
    })

if __name__ == "__main__":
    app.run(debug=True)