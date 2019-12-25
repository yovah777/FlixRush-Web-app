from django.urls import path
from django.conf.urls import include, url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile),
    url(r'^detail/(?P<id>\w{0,50})/$', views.detail,), # URL route detail/:id
]