from django.shortcuts import render,redirect
from app.models import Form

# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        form = Form(username=username,email=email,password=password)
        form.save()
        return render(request,'done.html')

    return render(request,"index.html")