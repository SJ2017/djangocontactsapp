from django.urls import path
from .import views
app_name = "appone"
urlpatterns = [
    path("",views.index,name="index"),
    path("forms/",views.formview,name="form"),
    path("deleteall/",views.deleteall,name='deleteall'),
    path("register",views.register,name='register'),
    path("login",views.userlogin,name='login'),
    path("logout",views.userlogout,name='logout'),
    path("special",views.special,name='special'),
    path("contacts",views.contactsview,name='contactsurl')
    
]
