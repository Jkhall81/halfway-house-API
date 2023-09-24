from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Router stuff
router = DefaultRouter()
router.register(r'houses', views.HouseViewSet)
router.register(r'residents', views.ResidentViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
