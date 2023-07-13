
from django.urls import path
from cart import views

app_name = 'cart'

urlpatterns = [

    path('', views.detail, name='detail'),
    path('add/<int:id>/',views.add, name='add_cart'),
    path('remove/<int:id>/',views.remove, name='remove_cart'),
]