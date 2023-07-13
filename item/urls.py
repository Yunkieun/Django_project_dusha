from django.urls import path

from item import views

app_name = 'item'


urlpatterns = [

    path('', views.item_list, name='item_list'),
    path('<int:id>', views.item_detail, name='item_detail'),

    path('create/', views.item_create, name='item_create'),
    path('category/<str:slug>/', views.category_page, name='category_page'),
    path('<int:id>/like/', views.like_vote, name='like_vote'),


    ]

