from django.urls import path, include
from rest_framework import routers

from Meter_rest.views import *


class CustomRouter(routers.SimpleRouter):
    routes = [
        routers.Route(url=r'^{prefix}/$',
                      mapping={'get': 'list', 'post': 'create'},  # Добавляем поддержку метода POST для создания
                      name='{basename}-list',
                      detail=False,
                      initkwargs={'suffix': 'List'}),
        routers.Route(url=r'^{prefix}/{lookup}$',
                      mapping={'get': 'retrieve', 'put': 'update', 'delete': 'destroy'},
                      # Добавляем поддержку методов PUT и DELETE
                      name='{basename}-detail',
                      detail=True,
                      initkwargs={'suffix': 'Detail'}),
    ]


router = CustomRouter()
router.register(r'data', DataViewSet, basename='data')
print(router.urls)

urlpatterns = [
    path('api/', include(router.urls))
]
