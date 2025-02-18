from django.contrib import admin
from django.urls import path, include  # include is important for adding app-specific URLs

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('conversion.urls')),  # Include conversion app URLs here
]
from django.urls import path, include
from conversion.views import conversion_page  # Import the view for home page

urlpatterns = [
    path('', conversion_page, name='home'),  # Add this line for home page
    path('admin/', admin.site.urls),
    path('api/', include('conversion.urls')),  # Make sure this is here
]
