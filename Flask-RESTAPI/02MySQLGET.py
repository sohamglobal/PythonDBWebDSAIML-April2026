from flask import Flask,jsonify
import pymysql

app=Flask(__name__)

@app.route('/doctors',methods=['GET'])
def getalldoctors():
    connection=pymysql.connect(host='mysql-27706bd3-praffull-project.d.aivencloud.com',port=14602,user='avnadmin',password='AVNS_yyFqLbIXvQq6c_LMztu',database='defaultdb',cursorclass=pymysql.cursors.DictCursor)
    cursor=connection.cursor()
    cursor.execute("select * from doctors")
    data=cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(data)

@app.route('/accounts/<type>',methods=['GET'])
def getaccounts(type):
    connection=pymysql.connect(host='mysql-27706bd3-praffull-project.d.aivencloud.com',port=14602,user='avnadmin',password='AVNS_yyFqLbIXvQq6c_LMztu',database='defaultdb',cursorclass=pymysql.cursors.DictCursor)
    cursor=connection.cursor()
    cursor.execute(f"select * from accounts where acctype='{type}'")
    data=cursor.fetchall()
    cursor.close()
    connection.close()
    return jsonify(data)

app.run(debug=True)
