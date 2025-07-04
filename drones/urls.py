from django.urls import path
from . import views



urlpatterns = [
    # Drone Categories
    path('drone-categories/', views.DroneCategoryList.as_view(), name=views.DroneCategoryList.name),
    path('drone-categories/<int:pk>/', views.DroneCategoryDetail.as_view(), name=views.DroneCategoryDetail.name),

    # Drones
    path('drones/', views.DroneList.as_view(), name=views.DroneList.name),
    path('drones/<int:pk>/', views.DroneDetail.as_view(), name=views.DroneDetail.name),

    # Pilots
    path('pilots/', views.PilotList.as_view(), name=views.PilotList.name),
    path('pilots/<int:pk>/', views.PilotDetail.as_view(), name=views.PilotDetail.name),

    # Competitions
    path('competitions/', views.CompetitionList.as_view(), name=views.CompetitionList.name),
    path('competitions/<int:pk>/', views.CompetitionDetail.as_view(), name=views.CompetitionDetail.name),

    # Root endpoint
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]
