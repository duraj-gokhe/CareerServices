from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Portal.urls.Staff')),
    path('',include('Portal.urls.Login'))
]
