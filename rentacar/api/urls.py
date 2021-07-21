from django.urls import path
from . import views

app_name = 'clients'

urlpatterns = [
    path('clients/',
        views.ClientListView.as_view(),
        name='subject_list'),
]