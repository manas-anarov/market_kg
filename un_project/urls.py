
from django.contrib import admin
from django.urls import path

from django.conf.urls import include, url

from django.conf.urls.static import static
from django.conf import settings

from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('un-shop/', include(('un_shop.urls', 'api-un-shop'), namespace='api-un-shop')),
    # path('', include(('un_shop.urls', 'un_shop'), namespace='un_shop')),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

