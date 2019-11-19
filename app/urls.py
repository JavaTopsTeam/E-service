from django.urls import path,include
from . import views
urlpatterns = [
   
   path("",views.IndexPage,name="indexpage"),
   path("registeruser/",views.registerUser,name="register"),
   path("all_details/",views.AllDetails,name="alldetail"),
]
