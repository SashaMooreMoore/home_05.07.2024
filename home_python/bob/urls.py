from django.urls import path
from . import views

urlpatterns = [
    path('', views.BobSession.as_view())
]