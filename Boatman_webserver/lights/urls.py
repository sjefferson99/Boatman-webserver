from django.urls import path

from . import views

app_name = 'lights'
urlpatterns = [
    path('', views.index, name='index'),
    path('light/<int:id>/', views.light_detail, name='light_detail'),
    path('group/<int:id>/', views.group_detail, name='group_detail'),
    path('bmcomms/', views.bmcomms, name='bmcomms'),
]