from django.urls import path,include, re_path
from . import views
from .views import *

urlpatterns= [
    path('', views.index, name= 'index'),
    path('model-add', views.add_model, name= 'add'),
    path('model-view', views.view_model, name= 'view'),
]