from django.urls import path

from .views import index, by_station

urlpatterns = [
	path('<int:subsidiary_id>/', by_station),
	path('', index, name='index'),
]