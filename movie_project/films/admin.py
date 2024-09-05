# films/admin.py

from django.contrib import admin
from .models import Film

# Регистрация модели Film в админке
admin.site.register(Film)
