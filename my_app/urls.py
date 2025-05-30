from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'universities', UniversityViewSet)
router.register(r'faculties', FacultyViewSet)
router.register(r'chairs', ChairViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'students', StudentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
