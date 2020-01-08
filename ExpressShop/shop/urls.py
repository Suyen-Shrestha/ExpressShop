from django.urls import path, include
from .views import HomeView, ItemDetailView, add_to_cart

app_name = 'shop'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/<slug>/', ItemDetailView.as_view(), name='item_detail'),
    path('add-to-cart/<slug>', add_to_cart, name='add-to-cart'),

]