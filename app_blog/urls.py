from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from app_blog import views

urlpatterns = [
    path(r"", views.HomePageView.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
