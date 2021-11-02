from django.urls import path
from members.views import home_view

urlpatterns = [
    path('', home_view, name='home_page'),
]