
from django.urls import path

from coupon import views

app_name = 'coupon'

urlpatterns = [

    path('add/', views.add_coupon, name='add'),

]