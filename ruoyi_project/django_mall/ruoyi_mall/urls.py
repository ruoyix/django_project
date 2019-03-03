from django.urls import path
from ruoyi_mall import views as v
from django.contrib.auth.views import *

app_name = 'ruoyi_mall'   # mall:login
urlpatterns = [
    path('register/', v.register_view, name='register'),
    path('createsuperuser/', v.createsuperuser_view, name='createsuperuser'),
    path('login/', v.MyLoginView.as_view(), name='login'),
    path('logout/', v.MyLogoutView.as_view(), name='logout'),
    path('password_change/', v.MyPasswordChangeView.as_view(), name='password_change'),
    path('index/', v.index_view, name='index'),
    path('detail/', v.detail_view, name='detail'),
    path('shopcar_add/', v.shopcar_add_view, name='shopcar_add'),
    path('shopcar/', v.shopcar_view, name='shopcar'),
]