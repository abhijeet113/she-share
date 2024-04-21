from django.contrib import admin
from django.urls import path
from Wairbnb import views
urlpatterns = [
    path("" ,views.index,name='index'),
    path("login",views.login,name='login'),
    path("shareproperty",views.shareproperty,name='shareproperty'),
    path("rentproperty",views.rentproperty,name='rentproperty'),
    path("profile",views.profile,name="profile"),
    path("stories",views.stories,name="stories"),
    path("registration/",views.registration,name="registration"),
]
