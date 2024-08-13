from django.urls import path
from . import views


urlpatterns = [
 path('', views.index, name='index'),
 path('about/', views.about, name='about'),
 path('statistic/', views.statistic, name='statistic'),
 path('transient/<int: >', views.transient, name='transient'),
 path('edit/', views.edit, name='edit'),
]
