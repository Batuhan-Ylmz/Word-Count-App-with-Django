from django.urls import path
from . import views
from .views import counter
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('counter', views.counter, name = 'counter'),
    path('', views.counter, name = 'counter')
    

]