from django.shortcuts import render
from datetime import date

def home(request):
    return render(request,"index.html")

def newcomplaint(request):
    return render(request,"newcomplaint.html")

def complistform(request):
    # fetch all complaints from the db
    return render(request,"complistform.html")

def addcomplaint(request):
    if request.method=="POST":
        ano=request.POST.get("account_number")
        nm=request.POST.get("name")
        cat=request.POST.get("category")
        pr=request.POST.get("priority")
        comp=request.POST.get("complaint")
        dic={}
        dic['accno']=ano
        dic['name']=nm
        dic['category']=cat
        dic['priority']=pr
        dic['complaint']=comp
        dic['compdate']=date.today()
        dic['status']='progress'
        print(dic)
        # insert into mongodb collection
    return render(request,"complaintadded.html")