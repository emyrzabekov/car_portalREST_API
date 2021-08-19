from django.urls import path
from .views import CarListView, CarDetailGenericView

urlpatterns = [
    path('car_list/', CarListView.as_view()),
    path('cars/<int:id>/', CarDetailGenericView.as_view()),
]
