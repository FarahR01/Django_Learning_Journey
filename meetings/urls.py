from django.urls import path
from . import views

#Lister les meetings : http://127.0.0.1:8000/meetings/list
urlpatterns = [
    path('list', views.meeting_list, name='meeting_list'),     # URL pour la vue meeting_list

    path('<int:id>/', views.detail, name='detail'),  # URL pour afficher les détails

    path('delete/<int:id>/' ,views.delete_meeting, name='delete_meeting'),  # URL pour supprimer un meeting
]
