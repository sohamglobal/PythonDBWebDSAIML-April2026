from flask import Flask,jsonify
from pymongo import MongoClient
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

# MongoDB connectivity

client=MongoClient("mongodb+srv://praffull:mongodb913@sharayucluster.dpfu46o.mongodb.net/?appName=SharayuCluster")
db=client["spiderdb"]
coll=db["films"]
coll1=db["players"]

@app.route('/films',methods=['GET'])
def getfilms():
    films=list(coll.find())
    # convert ObjectId to string
    for f in films:
        f["_id"]=str(f["_id"])
    return jsonify(films)

@app.route('/players',methods=['GET'])
def getplayers():
    players=list(coll1.find())
    return jsonify(players)



app.run(debug=True)
