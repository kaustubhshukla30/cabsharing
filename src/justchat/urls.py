from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path, include
from bookings import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='home'),
    path('chat/', include('chat.urls', namespace='chat')),
    path('accounts/', include('accounts.urls')),
    path('bookings/', include('bookings.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
