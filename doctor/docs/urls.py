from django.urls import path

from docs import views

urlpatterns=[
    path('index',views.index,name='index'),
    path('search', views.search, name='search')
]