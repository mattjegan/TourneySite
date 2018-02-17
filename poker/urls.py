from django.conf.urls import url

from . import views

app_name = 'poker'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blinds/', views.blindsStructure, name='blinds'),
    url(r'^stackCalc/', views.stackCalculator, name='stackCalc'),
    url(r'^chipDist/', views.chipDistribution, name='chipDist'),
    url(r'^prizeDist/', views.prizePoolDistribution, name='prizeDist'),
    url(r'^processBlinds/', views.processBlinds, name='processBlinds'),
    url(r'^processChipDist/', views.processChipDist, name='processChipDist'),
    url(r'^processStackCalc/', views.processStackCalc, name='processStackCalc'),
    url(r'^processPrize/', views.processPrize, name='processPrize'),
]