from django.contrib import admin

# Register your models here.
from .models import Rent


class RentAdmin(admin.ModelAdmin):

    list_display = ('company', 'client', 'daily_cost', 'days') 


admin.site.register(Rent, RentAdmin)