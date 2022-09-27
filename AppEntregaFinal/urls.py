from django.urls import path
from AppEntregaFinal.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path("",Inicio,name="home"),
    path("register/",register_request,name="register"),
    path("login/",login_request,name="login"),
    path("logout/", LogoutView.as_view(template_name="logout.html"),name="logout"),
    path("post1/",post1,name="post1"),
    path("post2/",post2,name="post2"),
    path("post3/",post3,name="post3"),
    path("post4/",post4,name="post4"),
    path("contacto/",Contactar,name="contacto"),
    path("about/",About,name="about"),

    

]