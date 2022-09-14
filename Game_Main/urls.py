from django.urls import path

from Game_Main import views

urlpatterns = [
    path("",views.MainPage,name="MainPageUrl"),
    path("MoveToCity/<str:id>",views.MoveToCity),
    path("TraveIsDone/",views.TraveIsDone,name="TraveIsDoneUrl"),
    path("SellProduct/",views.SellProductInCity)
]  