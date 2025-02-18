# conversion/urls.py
from django.urls import path
from .views import convert_value

urlpatterns = [
    path('convert/', convert_value, name='convert_value'),  # Correct URL pattern
]
# urls.py
from django.urls import path
from .views import conversion_page, convert_value

urlpatterns = [
    path('', conversion_page, name='conversion_page'),  # Root URL for the form
    path('api/convert/', convert_value, name='convert_value'),  # API endpoint
]

