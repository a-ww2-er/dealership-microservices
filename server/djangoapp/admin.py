from django.contrib import admin
from .models import CarMake, CarModel


class CarModelInline(admin.TabularInline):

    model = CarModel


class CarModelAdmin(admin.ModelAdmin):

    list_display = ('name', 'car_make', 'type', 'year')
    list_filter = ('car_make', 'type', 'year')
    search_fields = ('name', 'car_make__name')
    ordering = ('car_make', 'name')
    raw_id_fields = ('car_make',)


class CarMakeAdmin(admin.ModelAdmin):

    list_display = ('name', 'country', 'website')
    search_fields = ('name', 'country')
    inlines = [CarModelInline]


admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
