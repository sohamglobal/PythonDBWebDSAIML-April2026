from django.shortcuts import render, redirect
import pymysql

def homepage(request):
    return render(request,"index.html")

def login(request):
    if request.method=="POST":
        uid=request.POST.get("userid")
        ps=request.POST.get("password")
        connection=pymysql.connect(host='mysql-27706bd3-praffull-project.d.aivencloud.com',port=14602,user='avnadmin',password='AVNS_yyFqLbIXvQq6c_LMztu',database='defaultdb')
        cursor=connection.cursor()
        cursor.execute(f"select * from users where userid='{uid}' and password='{ps}'")
        data=cursor.fetchone()
        connection.close()
        if data:
            return redirect("/recruiterhome/")
        else:
            return redirect("/failure/")
    return redirect("/jobs/")

def rechome(request):
    return render(request,"recruiteradmin.html")

def failure(request):
    return render(request,"failure.html")

