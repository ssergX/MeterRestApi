from django.urls import path
from Meter_rest import views

urlpatterns = [
    path('api/data/', views.DataViewSet.as_view()),
    path('api/data/<int:id>/', views.DataDetailViewSet.as_view()),
]
