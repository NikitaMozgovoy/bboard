from django.urls import path
from rest_framework import routers
from .views import BbViewSet, BbRubricViewSet, index

urlpatterns = [
    path('temp/', index),
]

router = routers.SimpleRouter()
router.register('bboard', BbViewSet, basename = 'bbs')
router.register('categories',BbRubricViewSet, basename='categories')
urlpatterns += router.urls