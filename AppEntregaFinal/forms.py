from django import forms
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User 


#FORMULARIO DE REGISTRO
class UserRegisterForm (UserCreationForm):
    class UserRegisterForm(UserCreationForm):
      email= forms.EmailField()
      username= forms.CharField()
      password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
      password2= forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)

    class Meta:
        model= User
        fields=["username", "email", "password1", "password2"]
        help_texts={k:"" for k in fields}





