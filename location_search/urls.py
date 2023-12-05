from django.urls import path
from . import views

urlpatterns = [
    path('', views.map_view, name='findGas'),
    # Other paths go here
    path('search',views.submit, name='submit'),
    path('searchPage', views.searchPage, name='searchPage'),
    path('updatePrice/<int:gas_station_id>', views.updatePrice, name = 'updatePrice'),
    

    
]