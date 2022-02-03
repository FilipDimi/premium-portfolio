from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # Custom URLS
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('works/', views.works, name='works'),
    path('contact/', views.contact, name='contact'),
    path('project/<int:pk>/', views.detail_project, name='detail_project')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)