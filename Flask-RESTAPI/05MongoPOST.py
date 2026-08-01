from flask import Flask,jsonify,request
from pymongo import MongoClient
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

# MongoDB connectivity

client=MongoClient("mongodb+srv://praffull:mongodb913@sharayucluster.dpfu46o.mongodb.net/?appName=SharayuCluster")
db=client["spiderdb"]
coll=db["players"]

@app.route('/player/add',methods=['POST'])
def add_player():
    data=request.get_json()
    result=coll.insert_one(data)
    return jsonify({
        'message':'new player added'
    })

app.run(debug=True)