from django.urls import path

from . import views


urlpatterns = [

    path('upload/',views.upload , name = 'upload'),

    path('plt/',views.show , name = "choose"),
    path('nbiot/',views.nbiott,name = "nbiot")



]