from django.urls import path
from .views import login_view, index_view, index2_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('index/', index_view, name='index'),
    path('index2/', index2_view, name='index2'),
]