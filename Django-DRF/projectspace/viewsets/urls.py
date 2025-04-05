from django.urls import path, include
from viewsets import views
from viewsets.views import MobileViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'mobile',MobileViewSet,basename='mobile')


urlpatterns = [
    path('',include(router.urls))
]