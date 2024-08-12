from django.urls import path
from main import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='home'),
    path('tours/<str:name>', views.tours, name='tours'),
    path('tours/tour', views.tour, name='tour'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)