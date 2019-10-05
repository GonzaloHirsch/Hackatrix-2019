from flask import Flask
from flask_pymongo import PyMongo

# APP config
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/db"
mongo = PyMongo(app)

problems

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
def insert():
    # database
    db = mongo.db

    # Hace todos los inserts
    insertAllProblems(db)
    insertAllTips(db)
    insertAllMaterials(db)

    return "done"

@app.route("/insertextra")
def insert():
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
    cProblems = db.problems
    for problem in problems:
        cProblems.insert_one(problem)
    return

def insertAllTips(db):
    cTips = db.tips
    for tip in tips:
        cTips.insert_one(tip)
    return

def insertAllMaterials(db):
    cMaterials = db.materials
    for material in materials:
        cMaterials.insert_one(material)
    return

# -------------------- GETTERS -------------------

#Get the tips by category
@app.route("/tips")
def getTipCategories():
	data		= mongo.db.tips.find()
    dataArray 	= cursorToArray(data)
    return str(dataArray)


#Get the tips by category
@app.route("/tips/<category>")
def getTipByCategory(category):
	myquery 	= {"category": category}
	data		= mongo.db.tips.find(myquery)
    dataArray 	= cursorToArray(data)
    return str(dataArray)

# Get all the problems
@app.route("/problems/<id>")
def getProblemById(id):
	myquery 	= {"id": self.id}
	database	= mongo.db.problems.find(myquery)
    dataArray 	= cursorToArray(data)
    return str(dataArray[0])

#Get a specific problem by id
@app.route("/problems")
def getProblems():
	database	= mongo.db.problems.find()
    dataArray 	= cursorToArray(data)
    return str(dataArray)

#Get the tips by category
@app.route("/materials")
def getMaterials():
	data		= mongo.db.tips.find()
    dataArray 	= cursorToArray(data)
    return str(dataArray)

# Recycling materials and subcategories
@app.route("/materials/<category>")
def getMaterialSubcategory(category):
	myquery 	= {"category": category}
	data		= mongo.db.materials.find(myquery)
    dataArray 	= cursorToArray(data)
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
