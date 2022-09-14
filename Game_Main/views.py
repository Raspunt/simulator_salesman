from itertools import product
import json

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt


from . models import City,Product,Dealer,Events

def MainPage(requests):
    Citys = City.objects.all()

    return render(requests,'Game_Main/index.html',
    {
        'Citys':Citys
    })


def MoveToCity(requests,id):
    
    city = City.objects.get(id=id)
    events = Events.objects.all()
    
    # eventJson = []
    # for event in events:
    #     evDict = {}
    #     evDict['title'] = event.title
    #     evDict['Waysted_days'] = event.Waysted_days
    #     eventJson.append(evDict)


    return render(requests,"Game_Main/MoveToCity.html",
    {
        'city':city,
    })

 


def TraveIsDone(requests):

    dealer = Dealer.objects.get(id=1)


    dealer_products = dealer.telega_products

    return render(requests,'Game_Main/TravelsDone.html',
    {
        'dealer':dealer,
        'products':dealer_products.all()
    })

@csrf_exempt
def SellProductInCity(requests):

    dealer = Dealer.objects.get(id=1)

    print(dealer)

    # if requests.method == "POST":

    #     product = Product.objects.get(id=requests.POST['city_id'])

    #     dealer.money
        

# -Сделано-
# Выбор города
# База данных уже сделана
# События

# -Не сделано- 
# Главная страница
# Продажа продуктов
# Проработать взаимодействия с телегой
# Выбор продуктов на продажу

# -Проблемы- 
# немогу коректно перевести продукты из бд в json
