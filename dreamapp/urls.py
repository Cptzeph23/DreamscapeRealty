
from django.contrib import admin
from django.urls import path
from dreamapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('agents/', views.agents, name='agents'),
    path('contact/', views.contact, name='contact'),
    path('properties/', views.properties, name='properties'),
    path('singleProperty', views.singleProperty, name='singleProperty'),
    path('servicedetails/', views.servicedetails, name='servicedetails'),
    path('services/', views.services, name='services'),
    path('hunting/', views.hunting, name='hunting'),
    path('listing/', views.listing, name='listing'),
    path('marketing/', views.marketing, name='marketing'),
    path('negotiation/', views.negotiation, name='negotiation'),
    path('transaction/', views.transaction, name='transaction'),
    path('valuation/', views.valuation, name='valuation'),
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('kitengela/', views.kitengela, name='kitengela'),
    path('karenHardy/', views.karenHardy, name='karenHardy'),
    path('kilimani/', views.kilimani, name='kilimani'),
    path('kitsuru/', views.kitsuru, name='kitsuru'),
    path('westlands/', views.westlands, name='westlands'),
    path('runda/', views.runda, name='runda'),
    path('pay/', views.pay, name='pay'),
    #path('newproperty/', views.newproperty, name='newproperty'),

    path('pay/', views.pay, name='pay'),
    path('stk/', views.stk, name='stk'),
    path('token/', views.token, name='token'),



]
