from django.urls import path

from order import views

app_name = 'order'


urlpatterns = [
    path('create/', views.order_create, name='order_create'),
    path('complete/', views.order_complete, name='order_complete'),
    path('create/<int:id>',views.order_form, name='order_form')

    ]

