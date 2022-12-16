from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from Trello.views import home_page


urlpatterns = [
    path('', home_page, name='home_page'),
    path('admin/', admin.site.urls),
    path('auth/', include("authentication.urls")),
    path('project/', include('project.urls')),
    path('landing/', include('landing.urls')),
    path('task/', include('task.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
