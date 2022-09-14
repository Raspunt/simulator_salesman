from itertools import product
import json

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect


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

 


def MovingDone(requests,city_id):

    city = City.objects.get(id=city_id)
    dealer = Dealer.objects.get(id=1)

    city_products = city.products.all()
    dealer_products = dealer.products.all()

    return render(requests,'Game_Main/MovingDone.html',
    {
        'city':city,
        'dealer':dealer,
        'dealer_products':dealer_products,
        'city_products':city_products
    })

@csrf_exempt
def SellProductInCity(requests,city_id,product_id):

    if requests.method == "POST":

        dealer = Dealer.objects.get(id=1)
        city = City.objects.get(id=city_id)
        product = Product.objects.get(id=product_id)

        city.products.add(product)
        dealer.products.remove(product)
        dealer.money += product.cost
        dealer.save()
        

        city = City.objects.get(id=city_id)
        dealer = Dealer.objects.get(id=1)

        city_products = city.products.all()
        dealer_products = dealer.products.all()

        print(dealer)
        print(requests.POST)

        return render(requests,'Game_Main/MovingDone.html',
        {
            'city':city,
            'dealer':dealer,
            'dealer_products':dealer_products,
            'city_products':city_products
        })


@csrf_exempt
def BuyProductInCity(requests,city_id,product_id):

    if requests.method == "POST":

        dealer = Dealer.objects.get(id=1)
        city = City.objects.get(id=city_id)
        product = Product.objects.get(id=product_id)


        if dealer.money >= product.cost:
 
            city.products.remove(product)
            dealer.products.add(product)
            dealer.money -= product.cost
            dealer.save()
        
            city = City.objects.get(id=city_id)
            dealer = Dealer.objects.get(id=1)

            city_products = city.products.all()
            dealer_products = dealer.products.all()


            return render(requests,'Game_Main/MovingDone.html',
            {
                'city':city,
                'dealer':dealer,
                'dealer_products':dealer_products,
                'city_products':city_products
            })
        else :
            return HttpResponse("не хватает денег")
                





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
