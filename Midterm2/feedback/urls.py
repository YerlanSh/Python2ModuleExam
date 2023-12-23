from django.urls import path
from .views import home, feedback

urlpatterns = [
    path('', home, name='home'),
    path('feedback/', feedback, name='feedback'),
]
