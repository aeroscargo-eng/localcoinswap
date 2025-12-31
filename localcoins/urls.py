from django.contrib import admin  # Import admin module from Django
from django.urls import include, path
from core.views import login_view, index_view, index2_view  # Import views

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin URL
    path('', index_view, name='home'),  # Optional: root URL
    path('login/', login_view, name='login'),  # Login page
    path('index/', index_view, name='index'),  # Index page
    path('index2/', index2_view, name='index2'),  # Index2 page
]