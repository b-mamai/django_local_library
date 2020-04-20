from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
]
# Используйте include() чтобы добавлять URL из каталога приложения
from django.urls import include
from django.urls import path
urlpatterns += [
     path('catalog/', include('catalog.urls')),
]


# Добавьте URL соотношения, чтобы перенаправить запросы с корневового URL, на URL приложения
from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
]

# Используйте static() чтобы добавить соотношения для статических файлов
# Только на период разработки
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
