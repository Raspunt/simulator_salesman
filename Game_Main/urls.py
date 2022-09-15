from django.urls import path

from Game_Main import views

urlpatterns = [
    path("",views.MainPage),
    path("ListCitys/",views.ListCitys,name="listCitysUrl"),
    path("MoveToCity/<str:id>",views.MoveToCity),
    path("MovingDone/<str:city_id>",views.MovingDone),
    path("SellProduct/<str:city_id>/<str:product_id>/<str:dealer_id>",views.SellProductInCity),
    path("BuyProduct/<str:city_id>/<str:product_id>/<str:dealer_id>",views.BuyProductInCity),
    path("GetDealerData/<str:dealer_id>",views.GetDealerData),
    path("GetEvents/",views.GetEvents)
]  