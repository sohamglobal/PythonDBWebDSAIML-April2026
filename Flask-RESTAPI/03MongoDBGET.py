from flask import Flask,jsonify
from pymongo import MongoClient

app=Flask(__name__)

# MongoDB connectivity

client=MongoClient("mongodb+srv://praffull:mongodb913@sharayucluster.dpfu46o.mongodb.net/?appName=SharayuCluster")
db=client["spiderdb"]
coll=db["films"]

@app.route('/films',methods=['GET'])
def getfilms():
    films=list(coll.find())
    return films


app.run(debug=True)
