from django.contrib import admin

from . models import Product,City,Dealer,Events

admin.site.register(Product)
admin.site.register(City)
admin.site.register(Dealer)
admin.site.register(Events)