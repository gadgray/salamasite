from os import name
from django.urls import path 
from . import views


urlpatterns=[ 
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('donation', views.donation, name='donation'),
    path('programs', views.programs, name='programs'),
    path('post<str:pk>', views.post, name='post'),
    path('youthpage', views.youthpage, name='youthpage'),
    path('download', views.download, name='download'),
    path('message', views.message, name='message'),
    path('pastorpost<str:pk>', views.pastorpost, name='pastorpost')
]