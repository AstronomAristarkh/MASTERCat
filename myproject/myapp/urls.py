from django.urls import path
from . import views


urlpatterns = [
 path('', views.index, name='index'),
 path('transients/', views.transients, name='transients'),
 path('statistic/', views.statistic, name='statistic'),
 path('transient/<int:number>/', views.transient, name='transient'),
 path('edit/', views.edit, name='edit'),
 path('ok/', views.ok, name='ok'),
 path('send/', views.send, name='send'),
 path('oke/', views.oke, name='oke'),
]
