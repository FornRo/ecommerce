from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include(('shop.urls', 'shop'))),
    path('', RedirectView.as_view(url='/shop/', permanent=True)),

]
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

#  static_file
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
