from django.urls import path
from . import views


urlpatterns = [
	path(r'/', views.parse_news, name='parse_news'),
	]