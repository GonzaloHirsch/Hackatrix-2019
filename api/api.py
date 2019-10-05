from flask import Flask
from flask_pymongo import PyMongo
import json

# APP config
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/db"
mongo = PyMongo(app)

extraProblem = {
"imageUrl": "https://www.nuevatribuna.es/media/nuevatribuna/images/2019/09/01/2019090108291259120.jpg",
"title": "Cambio climático",
"description": "Es la variación del clima de nuestro planeta, el cual siempre tuvo un comportamiento cíclico relativamente lento y en los últimos tiempos se vio abruptamente acelerado a causa del calentamiento global.",
"causes": [
"Efecto invernadero",
"Deforestación",
"Destrucción de ecosistemas marinos",
"Aumento de la población"
],
"consequences": [
"Cambios en ecosistemas y desertificación",
"Derretimiento de los polos y subida del nivel del mar",
"Riesgos en la salud humana",
"Especies en peligro de extinción y migraciones masivas",
"Fenómenos meteorológicos extremos"
],
"howToHelp": [
"Reducí el consumo eléctrico: apagá las luces, desenchufá los aparatos que no estés usando, usá lámparas LED, colgá la ropa en vez de usar secarropas, etc.",
"Ahorrá agua: duchate en 5 minutos, usá el programa de lavado que use menos agua, etc.",
"Usá los sistemas de calefacción solo si es necesario"
]
}

@app.route("/")
def home_page():
    data 	  = mongo.db.info.find()
    dataArray = cursorToArray(data)
    print(dataArray)
    # return render_template("index.html",
    #     online_users=online_users)
    return str(dataArray)

# -------------------- DELETES -------------------

# Borra la base de datos
@app.route("/delete")
def delete():
    # database
    db = mongo.db

    # Borra la base
    deleteAllProblems(db)
    deleteAllTips(db)
    deleteAllMaterials(db)

    return "done"

def deleteAllProblems(db):
    db.problems.remove({ })
    return

def deleteAllTips(db):
    db.tips.remove({ })
    return

def deleteAllMaterials(db):
    db.materials.remove({ })
    return

# -------------------- INSERTS -------------------

@app.route("/insertall")
def insertall():
    # database
    db = mongo.db

    # Hace todos los inserts
    insertAllProblems(db)
    insertAllTips(db)
    insertAllMaterials(db)

    return "done"

@app.route("/insertextra")
def insertextra():
    # database
    db = mongo.db

    # Hace el insert del extra
    insertExtraProblem(db)

    return "done"

def insertExtraProblem(db):
    cProblems = db.problems
    cProblems.insert_one(extraProblem)
    return

def insertAllProblems(db):
    with open('../info/Problemas.json') as file:
        print(file)
        problems = json.load(file)
        cProblems = db.problems
        for problem in problems:
            cProblems.insert_one(problem)
    return

def insertAllTips(db):
    with open('../info/Tips.json') as file:
        print(file)
        tips = json.load(file)
        cTips = db.tips
        for tip in tips:
            cTips.insert_one(tip)
    return

def insertAllMaterials(db):
    with open('../info/Reciclaje.json') as file:
        print(file)
        materials = json.load(file)
        cMaterials = db.materials
        for material in materials:
            cMaterials.insert_one(material)
    return

# -------------------- GETTERS -------------------

#Get the tips by category
@app.route("/tips")
def getTipCategories():
    data = mongo.db.tips.find()
    dataArray = cursorToArray(data)
    return str(dataArray)

#Get the tips by category
@app.route("/tips/<category>")
def getTipByCategory(category):
    myquery = {"category": category}
    data = mongo.db.tips.find(myquery)
    dataArray = cursorToArray(data)
    return str(dataArray)

# Get all the problems
@app.route("/problems/<id>")
def getProblemById(id):
    myquery = {"id": self.id}
    data = mongo.db.problems.find(myquery)
    dataArray = cursorToArray(data)
    return str(dataArray[0])

#Get a specific problem by id
@app.route("/problems")
def getProblems():
    data = mongo.db.problems.find()
    dataArray = cursorToArray(data)
    return str(dataArray)

#Get the tips by category
@app.route("/materials")
def getMaterials():
    data = mongo.db.materials.find()
    dataArray = cursorToArray(data)
    return str(dataArray)

# Recycling materials and subcategories
@app.route("/materials/<category>")
def getMaterialSubcategory(category):
    myquery = {"category": category}
    data = mongo.db.materials.find(myquery)
    dataArray = cursorToArray(data)
    return str(dataArray)

# -------------------- UTILS -------------------

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
