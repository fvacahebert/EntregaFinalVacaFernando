#IMPORTS
from django.shortcuts import render
from django.http import HttpResponse
from AppEntregaFinal.forms import *

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 
from django.contrib.auth import login,logout,authenticate 


##################################################################################################################

#VISTA INICIO
def Inicio (request):
    return render(request, "inicio.html")

def post1 (request):
    return render(request, "post1.html")

def post2 (request):
    return render(request, "post2.html")

def post3 (request):
    return render(request, "post3.html")

def post4 (request):
    return render(request, "post4.html")



##################################################################################################################


# REGISTRO / LOGIN / LOGOUT

#Login
def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request,data=request.POST) 
        if form.is_valid():
            user=request.POST["username"]
            clave = request.POST["password"]

            usuario=authenticate(username=user, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, "inicio.html",{"mensaje":f"Bienvenido {usuario}"})
            else: 
                return render(request, "login.html",{"formulario":form, "mensaje":  "usuario o contraseña incorrectos"})
        else:
            return render(request, "login.html",{"formulario":form, "mensaje":  "usuario o contraseña incorrectos"})
    else: 
        form=AuthenticationForm()
        return render(request, "login.html", {"formulario":form})

#Registro
def register_request(request): 
    if request.method=="POST":
        form=UserRegisterForm(request.POST) 
        if form.is_valid():
            user=form.cleaned_data.get("username")  
            form.save() 
            return render(request, "inicio.html",{"mensaje":f"Usuario {user} creado correctamente"})
        else:
            return render(request, "register.html", {"formulario":form, "mensaje": "Error al crear el usuario, intentelo nuevamente"})

    else: 
        form=UserRegisterForm()
        return render(request, "register.html", {"formulario":form})



#Logout ---> Pasa por URL



##################################################################################################################