from django.conf.urls import include,url
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('' , include('pages.urls')),
    path('listings/' , include('listings.urls')),
    path('contacts/' , include('contacts.urls')),
    path('accounts/' , include('accounts.urls')),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
