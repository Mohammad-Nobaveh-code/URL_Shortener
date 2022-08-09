from django.urls import path
from . import views

urlpatterns = [
	path('', views.ShortenerApiView.as_view(), name='all_links'),
	path('make/', views.ShortenerCreateApiView.as_view(), name='make_api'),
]
