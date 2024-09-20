from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CarBrandView, CarDetailView, ProfileView, CarModelViewSet
router = DefaultRouter()
router.register(r'cars', CarModelViewSet)
urlpatterns = [
    path('api/', include(router.urls)),
    path('', CarBrandView.as_view()),
    path('<int:pk>/', CarDetailView.as_view()),
    path('profile/', ProfileView.as_view()),
]



