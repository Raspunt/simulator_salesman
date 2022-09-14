from django.urls import path

from Game_Main import views

urlpatterns = [
    path("",views.MainPage,name="MainPageUrl"),
    path("MoveToCity/<str:id>",views.MoveToCity),
    path("MovingDone/<str:city_id>",views.MovingDone,name="MovingDoneUrl"),
    path("SellProduct/<str:city_id>/<str:product_id>",views.SellProductInCity),
    path("BuyProduct/<str:city_id>/<str:product_id>",views.BuyProductInCity)
]  