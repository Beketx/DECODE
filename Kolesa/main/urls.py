from django.urls import path

from . import views


urlpatterns = [
    path('one/', views.One.as_view()),
    path('cars/', views.CarViewSet.as_view({'get': 'list'})),
    path('cars/add/', views.CarViewSet.as_view({'post': 'create'})),
    path('cars/detail/<str:id>/', views.CarViewSet.as_view({'get': 'detail'})),
    path('cars/update/<str:id>/', views.CarViewSet.as_view({'post': 'update'})),
    path('cars/delete/<str:id>/', views.CarViewSet.as_view({'post': 'delete'})),
    path('city/', views.CityViewSet.as_view({'get': 'list'})),
    path('city/add/', views.CityViewSet.as_view({'post': 'create'})),
    path('city/detail/<str:id>/', views.CityViewSet.as_view({'get': 'detail'})),
    path('city/update/<str:id>/', views.CityViewSet.as_view({'post': 'update'})),
    path('city/delete/<str:id>/', views.CityViewSet.as_view({'post': 'delete'})),
    path('category/', views.CategoryViewSet.as_view({'get': 'list'})),
    path('category/add/', views.CategoryViewSet.as_view({'post': 'create'})),
    path('category/detail/<str:id>/', views.CategoryViewSet.as_view({'get': 'detail'})),
    path('category/update/<str:id>/', views.CategoryViewSet.as_view({'post': 'update'})),
    path('category/delete/<str:id>/', views.CategoryViewSet.as_view({'post': 'delete'})),
    path('subcategory/', views.SubCategoryViewSet.as_view({'get': 'list'})),
    path('subcategory/add/', views.SubCategoryViewSet.as_view({'post': 'create'})),
    path('subcategory/detail/<str:id>/', views.SubCategoryViewSet.as_view({'get': 'detail'})),
    path('subcategory/update/<str:id>/', views.SubCategoryViewSet.as_view({'post': 'update'})),
    path('subcategory/delete/<str:id>/', views.SubCategoryViewSet.as_view({'post': 'delete'})),
    path('enginetype/', views.EngineTypeViewSet.as_view({'get': 'list'})),
    path('enginetype/add/', views.EngineTypeViewSet.as_view({'post': 'create'})),
    path('enginetype/detail/<str:id>/', views.EngineTypeViewSet.as_view({'get': 'detail'})),
    path('enginetype/update/<str:id>/', views.EngineTypeViewSet.as_view({'post': 'update'})),
    path('enginetype/delete/<str:id>/', views.EngineTypeViewSet.as_view({'post': 'delete'})),
    path('kp/', views.KPViewSet.as_view({'get': 'list'})),
    path('kp/add/', views.KPViewSet.as_view({'post': 'create'})),
    path('kp/detail/<str:id>/', views.KPViewSet.as_view({'get': 'detail'})),
    path('kp/update/<str:id>/', views.KPViewSet.as_view({'post': 'update'})),
    path('kp/delete/<str:id>/', views.KPViewSet.as_view({'post': 'delete'})),

]
