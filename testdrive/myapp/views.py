from django.shortcuts import render
from .forms import UserForm, CARS
from django.http import HttpResponse, HttpResponseRedirect
users = [
    {'name': 'Смирнов Д.В.',
     'phone': '8(905)222-33-12',
     'email': 'smirnov@gmail.com',
     'car': 'Nissan Murano'},
    {'name': 'Кузькин М.О.',
     'phone': '8(905)444-13-12',
     'email': 'kyzkinmax@gmail.com',
     'car': 'ВАЗ 2114'},
    {'name': 'Мартынов А.А.',
     'phone': '8(905)712-10-32',
     'email': 'Anbreymartynov6@gmail.com',
     'car': 'Vivo v12'}
]

def index(request):
    return render(request, "index.html", context={"users": users})

def about(request):
    return render(request, "about.html")

def record(request):
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = userform.cleaned_data["name"]
            phone = userform.cleaned_data["phone"]
            email = userform.cleaned_data["email"]
            car = int(userform.cleaned_data["car"])
            comment = userform.cleaned_data["comment"]
            car = list((filter(lambda elem: elem[0] == car, CARS)))[0][1]
            
            users.append({"name": name, "phone": phone, "email": email, "car": car,})
            return HttpResponseRedirect('/')
        else:
            return HttpResponse("Invalid data")
    else:
        userform = UserForm()
        return render(request, "record.html", {"form": userform})

