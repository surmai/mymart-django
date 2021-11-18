from django.urls import path
from . import views

#urls linked
urlpatterns = [
    path('', views.index)
]