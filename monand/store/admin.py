from django.contrib import admin

from .models import *

admin.site.register(Category)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(CardObject)
admin.site.register(Like)
admin.site.register(SubCategory)
