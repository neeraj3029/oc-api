from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('students', views.UserView)
router.register('complaints', views.ComplaintView)

urlpatterns = [
    path('', include(router.urls)),
]