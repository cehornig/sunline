from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('api/<str:lat>/<str:long>', views.api, name="api"),
    path('api/date/<str:lat>/<str:long>/<str:date>', views.api_date, name="api_date"),
]
