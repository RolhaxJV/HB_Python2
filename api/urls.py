"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from api.views import Detail_Table,List_Table,D_Date_Create,D_Cities_Create,D_Departement_Update

urlpatterns = [
    path('List/', List_Table.as_view(), name='list-table',),
    path('Detail/<str:table>/<str:pk>/', Detail_Table.as_view(), name='detail-tables'),

    path('create_date/', D_Date_Create.as_view(), name='create-date'),
    path('create_city/<str:postal_code>/',D_Cities_Create.as_view(),name='create-city'),
    path('update_departement/<str:pk>/',D_Departement_Update.as_view(),name='update-departement'),
]
