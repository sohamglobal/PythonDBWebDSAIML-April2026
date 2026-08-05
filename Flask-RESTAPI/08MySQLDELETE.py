from flask import Flask, request
import pymysql

app=Flask(__name__)

@app.route('/account/close',methods=['DELETE'])
def deleteaccount():
    ano=int(request.form.get("accnumber"))
    dic={}
    connection=pymysql.connect(host='mysql-27706bd3-praffull-project.d.aivencloud.com',port=14602,user='avnadmin',password='AVNS_yyFqLbIXvQq6c_LMztu',database='defaultdb',cursorclass=pymysql.cursors.DictCursor)
    cursor=connection.cursor()
    cnt=cursor.execute(f"delete from accounts where accno={ano}")
    if cnt==1:
        connection.commit()
        dic['status']='success'
    else:
        dic['status']='failed'
    connection.close()
    return dic

app.run(debug=True)

