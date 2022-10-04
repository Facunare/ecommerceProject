
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('addStock/', views.addStock, name='addStock'),
    path('buy/', views.buy, name="buy"),
    path('buy/<str:prod>/delete', views.delete_prod, name='delete_prod'),
]
