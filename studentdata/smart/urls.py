from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),
    path('students/', views.student_list, name='student_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
