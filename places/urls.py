from django.urls import path
from . import views

urlpatterns = [
        path('', views.map_view),
        path('<id>', views.location_view, name='location_view') 
    ]
