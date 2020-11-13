from django.urls import path
from .views import home, list_item, add_items

urlpatterns = [
    path('', home, name='home'),
    path('list/', list_item, name='list'),
    path('add/', add_items, name='add'),
]