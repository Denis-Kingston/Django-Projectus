# crudapp/urls.py

from django.urls import path,include

urlpatterns = [
    path('',include('crudapp.urls'))
]
    
