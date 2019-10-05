from flask import Flask
from flask_pymongo import PyMongo
from flask_cors import CORS
import utils as utils
import json

# APP config
app = Flask(__name__)
CORS(app)
app.config["MONGO_URI"] = "mongodb://localhost:27017/db"
mongo = PyMongo(app)

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
    deleteAllOrgs(db)

    return "done"

def deleteAllProblems(db):
    db.problems.remove({ })
    return

def deleteAllTips(db):
    db.tips.remove({ })
    return

def deleteAllOrgs(db):
    db.orgs.remove({ })
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
    insertAllOrganizaciones(db)

    return "done"

@app.route("/insertextra")
def insertextra():
    # database
    db = mongo.db

    # Hace el insert del extra
    insertExtraProblem(db)

    return "done"

def insertExtraProblem(db):
    with open('../info/ProblemaExtra.json') as file:
        extraProblem = json.load(file)
        cProblems = db.problems
        cProblems.insert_one(extraProblem)
    return

def insertAllProblems(db):
    with open('../info/Problemas.json') as file:
        problems = json.load(file)
        cProblems = db.problems
        for problem in problems:
            cProblems.insert_one(problem)
    return

def insertAllOrganizaciones(db):
    with open('../info/Organizaciones.json') as file:
        orgs = json.load(file)
        cOrgs = db.orgs
        for org in orgs:
            cOrgs.insert_one(org)
    return

def insertAllTips(db):
    with open('../info/Tips.json') as file:
        tips = json.load(file)
        cTips = db.tips
        for tip in tips:
            cTips.insert_one(tip)
    return

def insertAllMaterials(db):
    with open('../info/Reciclaje.json') as file:
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
    dataArray = utils.cursorToArray(data)
    return str(dataArray)

#Get the tips by category
@app.route("/orgs")
def getOrgs():
    data = mongo.db.orgs.find()
    dataArray = utils.cursorToArray(data)
    return str(dataArray)

#Get the tips by category
@app.route("/tips/<type>")
def getTipByCategory(type):
    myquery = {"type": type}
    data = mongo.db.tips.find(myquery)
    dataArray = utils.cursorToArray(data)
    return str(dataArray)

# Get all the problems
@app.route("/problems/<id>")
def getProblemById(id):
    myquery = {"id": self.id}
    data = mongo.db.problems.find(myquery)
    dataArray = utils.cursorToArray(data)
    return str(dataArray[0])

#Get a specific problem by id
@app.route("/problems")
def getProblems():
    data = mongo.db.problems.find()
    dataArray = utils.cursorToArray(data)
    return str(dataArray)

#Get the tips by category
@app.route("/materials")
def getMaterials():
    data = mongo.db.materials.find()
    dataArray = utils.cursorToArray(data)
    return str(dataArray)

# Recycling materials and subcategories
@app.route("/materials/<category>")
def getMaterialSubcategory(category):
    myquery = {"category": category}
    data = mongo.db.materials.find(myquery)
    dataArray = utils.cursorToArray(data)
    return str(dataArray)
