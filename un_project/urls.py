
from django.contrib import admin
from django.urls import path

from django.conf.urls import include, url

from django.conf.urls.static import static
from django.conf import settings

from django.conf.urls.static import static

from django.conf.urls.static import static

from un_shop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('un-shop/', include(('un_shop.urls', 'api-un-shop'), namespace='api-un-shop')),
	path('', views.CreateViewFront.as_view()),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

