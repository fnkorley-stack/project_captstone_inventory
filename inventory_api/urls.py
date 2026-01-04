from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),        # existing users app
    path('inventory/', include('inventory.urls')) # add this line
]
