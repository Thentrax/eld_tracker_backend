from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LogViewSet, CycleHoursViewSet

router = DefaultRouter()
router.register(r'logs', LogViewSet)
router.register(r'cycle_hours', CycleHoursViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('logs/<int:pk>/', LogViewSet.as_view({'get': 'get_by_id'}), name='log-detail'),
]
