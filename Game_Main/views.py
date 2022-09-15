from itertools import product
import json

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect


from . models import City,Product,Dealer,Events

def ListCitys(requests):
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
def SellProductInCity(requests,city_id,product_id,dealer_id):

    if requests.method == "POST":

        dealer = Dealer.objects.get(id=dealer_id)
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
def BuyProductInCity(requests,city_id,product_id,dealer_id):

    if requests.method == "POST":

        dealer = Dealer.objects.get(id=dealer_id)
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
                

def MainPage(requests):

    if requests.method == 'POST':

        print(requests.POST)

        name = requests.POST['name']
        telegaName = requests.POST['TelegaName']
        weightkg = requests.POST['weightkg']

        money = 20000

        dealer = Dealer.objects.create(delerName=name,money=money,telegaName=telegaName,weightkg=weightkg)
        Citys = City.objects.all()

        return render(requests,'Game_Main/index.html',
        {
            'Citys':Citys,
            'dealer':dealer
        })


    dealers = Dealer.objects.all()


        

    return render(requests,'Game_Main/MainPage.html',
    {
        'dealers':dealers
    })

@csrf_exempt
def GetDealerData(requests,dealer_id):

    if requests.method == "POST":
        dealer = Dealer.objects.get(id=dealer_id)

        return HttpResponse(f'{str(dealer.delerName).replace(" ","_")} {dealer.money}')


def GetEvents(requests):

    events = Events.objects.all()

    event_arr = []
    for event in events:

        event_str = f"{str(event.title).replace(' ','_')}*{event.Waysted_days}^"
        event_arr.append(event_str)

    return HttpResponse("".join(event_arr))    




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
