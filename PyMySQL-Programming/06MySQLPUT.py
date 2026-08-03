from flask import Flask,request
import pymysql
from flask_cors import CORS

app=Flask(__name__)
CORS(app)

@app.route('/user/change',methods=['PUT'])
def changepassword():
    uid=request.form.get("userid")
    cps=request.form.get("currpass")
    nps=request.form.get("newpass")
    dic={}
    connection=pymysql.connect(host='mysql-27706bd3-praffull-project.d.aivencloud.com',port=14602,user='avnadmin',password='AVNS_yyFqLbIXvQq6c_LMztu',database='defaultdb',cursorclass=pymysql.cursors.DictCursor)
    cursor=connection.cursor()
    cnt=cursor.execute(f"update users set password='{nps}' where userid='{uid}' and password='{cps}'")
    if cnt==1:
        dic['status']='success'
        connection.commit()
    else:
        dic['status']='failed'
    connection.close()
    return dic


app.run(debug=True)

