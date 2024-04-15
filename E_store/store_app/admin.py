from django.contrib import admin
from .models import *

class ImagesTabularInline(admin.TabularInline):
    model = Images

class TagTabularInline(admin.TabularInline):
    model = Tag

class ProductAdmin(admin.ModelAdmin):
    inlines = [ImagesTabularInline, TagTabularInline,]

class OrderItemTabularInline(admin.TabularInline):
    model = OrderItem

class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemTabularInline,]

admin.site.register(Images)
admin.site.register(Tag)

admin.site.register(Categories)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Filter_Price)
admin.site.register(Product, ProductAdmin)
admin.site.register(Contact_us)

admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
