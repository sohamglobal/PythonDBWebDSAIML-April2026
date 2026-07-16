from django.shortcuts import render

def homepage(request):
    return render(request,"index.html")

def docsinfo(request):
    return render(request,"doctors.html")

def contactinfo(request):
    return render(request,"contacts.html")
