from django.contrib import admin
from django.urls import path, include
from . import settings
from core.urls import core_urlpatterns
from services.urls import service_urlpatterns
from blog.urls import post_urlpatterns
from pages.urls import page_urlpatterns
from contact.urls import contact_urlpatterns

urlpatterns = [
    #path('', include('core,urls')),
    path('', include(core_urlpatterns)),
    path('services/', include(service_urlpatterns)),
    path('posts/', include(post_urlpatterns)),
    path('pages/', include(page_urlpatterns)),
    path('contact/', include(contact_urlpatterns)),
    path('admin/', admin.site.urls),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path('accounts/', include('django.contrib.auth.urls')),
]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)