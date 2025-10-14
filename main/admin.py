from django.contrib import admin
from .models import DishCategory,Dish,Gallary,Reservation,Chef,Event
admin.site.register(Reservation)
admin.site.register(Gallary)
admin.site.register(Chef)
admin.site.register(Event)


@admin.register(DishCategory)
class DishCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['id','name','category','is_visible', 'price']
    list_editable = ('name','category','is_visible', 'price')
    list_filter = ['category','price']
    search_fields = ['name']

