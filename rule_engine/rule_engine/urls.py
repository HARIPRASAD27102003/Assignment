from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rule-engine/', include('engine.urls')),  # Include the engine app's URLs
]
