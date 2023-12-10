from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
 

urlpatterns = [
    path('', receipt_list, name='receipt_list'),
    path('receipt/<int:pk>/', receipt_detail, name='receipt_detail'),
    path('receipt/new/', receipt_new, name='receipt_new'),
    path('receipt/<int:pk>/edit/', receipt_edit, name='receipt_edit'),
    path('login/', login_view, name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('home/', home, name='home'),

]
