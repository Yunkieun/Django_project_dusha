from django.contrib.auth import views as auth_views
from django.urls import path
from common import views

app_name = 'common'

urlpatterns = [
    path('<int:id>/', views.detail, name='detail'),
    path('signup/', views.CustomSignupView.as_view(), name='account_signup'),
    path('membership/', views.membership, name='membership'),
]
