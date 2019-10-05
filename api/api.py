from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/db"
mongo = PyMongo(app)

@app.route("/")
def home_page():
    data = mongo.db.info.find()[0]['name']
    print(data)
    # return render_template("index.html",
    #     online_users=online_users)
    return str(data)

@app.route("/insert")
def insert():

    # database
    db = mongo.db
    print("db")

    # Created or Switched to collection names: my_gfg_collection
    infoCollection = db.info

    print("col")
    info1 = {
            "name":"Mr.Geek",
            "eid":24,
            "location":"delhi"
            }
    info2 = {
            "name":"Mr.Shaurya",
            "eid":14,
            "location":"delhi"
            }

    print("preinsert")

    # Insert Data
    info1_id = infoCollection.insert_one(info1)
    info2_id = infoCollection.insert_one(info2)

    print("insert")
    return "done"
