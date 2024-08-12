from django.contrib import admin
from .models import Person, Country, Category, Another

admin.site.register(Person)
admin.site.register(Country)
admin.site.register(Category)
admin.site.register(Another)
