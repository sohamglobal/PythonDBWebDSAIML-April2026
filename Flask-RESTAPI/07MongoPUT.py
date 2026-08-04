from flask import Flask, request, jsonify
from pymongo import MongoClient

app=Flask(__name__)

client=MongoClient("mongodb+srv://praffull:mongodb913@sharayucluster.dpfu46o.mongodb.net/?appName=SharayuCluster")
db=client["spiderdb"]
coll=db["players"]

@app.route('/player/modify/<plid>',methods=['PUT'])
def updateplayer(plid):
    data=request.get_json()
    print(plid)
    print(data)
    if not data:
        return jsonify({"status":"no data found"}),400
    
    result=coll.update_one(
        {"_id":int(plid)},
        {"$set":data}
    )

    if result.matched_count==0:
        return jsonify({"status":"player not found"}),404
    
    return jsonify({
        "status":"player data modified"
    })


app.run(debug=True)