from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('students', views.UserView)

urlpatterns = [
    path('', include(router.urls)),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name="user-detail"),
]