from django.urls import path
from . import views

urlpatterns = [
    path('yes-its-api/', views.LogicApiView.as_view())
]
