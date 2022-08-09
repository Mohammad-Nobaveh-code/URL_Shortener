from django.contrib import admin
from django.urls import path
from django.urls.conf import include

from api.views import Redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('<str:shorten_link>/', Redirect.as_view(), name='redirector'),
]
