from django.urls import path

from . import views

urlpatterns = [
    path('favourites/', views.favorites_list),
    path('favourites/<int:favourite_id>/', views.favorites_detail),
    path('archive/', views.ArchiveAPIView.as_view()),
    path('publication/', views.PublicationsAPIView.as_view()),
    path('publication/<int:pub_id>/', views.PublicationsDetailAPIView.as_view())
]