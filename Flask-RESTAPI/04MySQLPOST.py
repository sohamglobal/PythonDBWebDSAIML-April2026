from flask import Flask,request
import pymysql

app=Flask(__name__)

@app.route('/user/add',methods=['POST'])
def add_user():
    uid=request.form.get("userid")
    psw=request.form.get("password")
    unm=request.form.get("usernm")
    dic={}
    try:
        connection=pymysql.connect(host='mysql-27706bd3-praffull-project.d.aivencloud.com',port=14602,user='avnadmin',password='AVNS_yyFqLbIXvQq6c_LMztu',database='defaultdb',cursorclass=pymysql.cursors.DictCursor)
        cursor=connection.cursor()
        cursor.execute(f"insert into users values('{uid}','{psw}','{unm}')")
        connection.commit()
        connection.close()
        dic['status']='success'
    except:
        dic['status']='failed'
    return dic

app.run(debug=True)
