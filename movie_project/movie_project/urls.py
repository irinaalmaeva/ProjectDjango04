# movie_project/urls.py

from django.contrib import admin
from django.urls import path
from films import views as films_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_film/', films_views.add_film, name='add_film'),
    path('', films_views.film_list, name='film_list'),
]

