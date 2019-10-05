from flask import Flask
from flask_pymongo import PyMongo

# APP config
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/db"
mongo = PyMongo(app)

@app.route("/")
def home_page():
    data = mongo.db.info.find()
    dataArray = cursorToArray(data)
    print(dataArray)
    # return render_template("index.html",
    #     online_users=online_users)
    return str(dataArray)

# Borra la base de datos
@app.route("/delete")
def delete():

    # database
    db = mongo.db
    print("db")

    # Created or Switched to collection names: my_gfg_collection
    db.info.remove({ })

    return "done"

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

# Pasa del cursor devuelto por Mongo a un array de diccionarios
def cursorToArray(cursor):
    elements = []
    for item in cursor:
        print(item)
        elements.append(cursorItemToDictionary(item))
    print(elements)
    return elements

# Pasa del diccionario que devuelve Mongo a otro sin el object ID
def cursorItemToDictionary(item):
    dic = {}
    for key in item.keys():
        if (key != '_id'):
            dic[key] = item[key]
    return dic
