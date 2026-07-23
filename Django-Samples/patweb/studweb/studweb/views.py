from django.shortcuts import render
import pymysql
from pymongo import MongoClient

def homepage(request):
    return render(request,"index.html")

def registerstud(request):
    return render(request,"newstudent.html")

def login(request):
    return render(request,"login.html")

def addstudent(request):
    if request.method=="POST":
        nm=request.POST.get("snm")
        co=request.POST.get("cou")
        fs=int(request.POST.get("fees"))
        print(f"{nm} | {co} | {fs}")
        connection=pymysql.connect(host='mysql-27706bd3-praffull-project.d.aivencloud.com',port=14602,user='avnadmin',password='AVNS_yyFqLbIXvQq6c_LMztu',database='defaultdb')
        cursor=connection.cursor()
        cursor.execute(f"insert into students(studnm,course,fees,admdt) values('{nm}','{co}',{fs},now())")
        connection.commit()
        connection.close()

    
    return render(request,"studentadded.html")

def showdata(request):
    cnm="core python"
    dur="5 weeks"
    fees=3000
    dic={}
    dic["coursenm"]=cnm
    dic["duration"]=dur
    dic["fees"]=fees
    print(dic)
    return render(request,"pythondata.html",dic)

def doclist(request):
    connection=pymysql.connect(host='mysql-27706bd3-praffull-project.d.aivencloud.com',port=14602,user='avnadmin',password='AVNS_yyFqLbIXvQq6c_LMztu',database='defaultdb')
    cursor=connection.cursor()
    cursor.execute("select * from doctors")
    data=cursor.fetchall()
    '''
    for doc in data:
        for val in doc:
            print(val)
    '''
    connection.close()
    dic={"docs":data}
    return render(request,"doctorsreport.html",dic)

def searchacc(request):
    if request.method=="POST":
        no=int(request.POST.get("ano"))
        connection=pymysql.connect(host='mysql-27706bd3-praffull-project.d.aivencloud.com',port=14602,user='avnadmin',password='AVNS_yyFqLbIXvQq6c_LMztu',database='defaultdb')
        cursor=connection.cursor()
        cursor.execute(f"select * from accounts where accno={no}")
        data=cursor.fetchone()
        dic={}
        if data:
            print(data)
            dic['number']=data[0]
            dic['name']=data[1]
            dic['type']=data[2]
            dic['balance']=data[3]
        else:
            print('not found')
            dic['number']=0
            dic['name']='Not Found'
            dic['type']='Not Found'
            dic['balance']='NA'
        connection.close()
    
    return render(request,"searchresult.html",dic)


def showworkers(request):
    client=MongoClient("mongodb+srv://praffull:mongodb913@sharayucluster.dpfu46o.mongodb.net/?appName=SharayuCluster")
    db=client["spiderdb"]
    coll=db["coworkers"]
    data=list(coll.find())
    return render(request,"workerslist.html",{"workers":data})

def newworker(request):
    return render(request,"add_worker.html")

def addworker(request):
    #receive and insert data
    return render(request,"workeradded.html")