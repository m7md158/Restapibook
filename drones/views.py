from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Pilot, Drone, Competition, DroneCategory
from .serializers import PilotSerializer, DroneSerializer, CompetitionSerializer, PilotCompetitionSerializer, DroneCategorySerializer
from rest_framework import filters
from django_filters import AllValuesFilter, DateFilter , NumberFilter
from .filters import CompetitionFilter

class DroneCategoryList(generics.ListCreateAPIView):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer
    name = 'dronecategory-list'
    
    filter_fields = ('name',)
    search_fields = ('^name',)
    ordering_fields = ('name',)
        

class DroneCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer
    name = 'dronecategory-detail'
    
    
class DroneList(generics.ListCreateAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = 'drone-list'
    
    filter_fields = ('name', 'drone_category', 'manufacturing_date', 'has_it_completed_missions')
    search_fields = ('^name',)
    ordering_fields = ('name','manufacturing_date')
    
    
class DroneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = 'drone-detail'
    
class PilotList(generics.ListCreateAPIView):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = 'pilot-list'
    
    filter_fields = ('name', 'gender', 'reces_count')
    search_fields = ('^name',)
    ordering_fields = ('name', 'reces_count')
    
class PilotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = 'pilot-detail'
    
    
class CompetitionList(generics.ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionSerializer
    name = 'competition-list'
    
class CompetitionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionSerializer
    name = 'competition-detail'
    filterset_class = CompetitionFilter
    ordering_fields = (
        'distance_in_feet', 
        'distance_achievement_date'
        )
    
    
    
class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'drone-categories': reverse(DroneCategoryList.name, request=request),
            'drones': reverse(DroneList.name, request=request),
            'pilots': reverse(PilotList.name, request=request),
            'competitions': reverse(CompetitionList.name, request=request),
        })