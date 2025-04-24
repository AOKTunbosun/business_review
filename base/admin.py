from django.contrib import admin
from .models import Business, Category, Review

# Register your models here.
admin.site.register(Business)
admin.site.register(Category)
admin.site.register(Review)