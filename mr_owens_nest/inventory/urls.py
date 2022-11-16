from django.urls import path
from .views import (
    ItemListView,
    ItemCreateView,
    ItemDetailView,
    ItemUpdateView,
    ItemDeleteView
)

app_name = 'inventory'

urlpatterns = [
    path('', ItemListView, name='list'),
    path('add/', ItemCreateView, name='create'),
    path('<slug:slug>', ItemDetailView, name='detail'),
    path('<slug:slug>/update', ItemUpdateView, name='update'),
    path('<slug:slug>/delete', ItemDeleteView, name='delete'),
]
