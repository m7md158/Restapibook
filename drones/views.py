from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Pilot, Drone, Competition, DroneCategory
from .serializers import PilotSerializer, DroneSerializer, CompetitionSerializer, PilotCompetitionSerializer, DroneCategorySerializer
from rest_framework import filters
from django_filters import AllValuesFilter, DateFilter , NumberFilter
from .filters import CompetitionFilter
from rest_framework import permissions
from  drones import custompermission
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.throttling import ScopedRateThrottle
from django_filters.rest_framework import DjangoFilterBackend


class DroneCategoryList(generics.ListCreateAPIView):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer
    name = 'dronecategory-list'
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ('name',)
    search_fields = ('^name',)
    ordering_fields = ('name',)
        

class DroneCategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DroneCategory.objects.all()
    serializer_class = DroneCategorySerializer
    name = 'dronecategory-detail'
    
    
class DroneList(generics.ListCreateAPIView):
    throttle_scope = 'drones'
    throttle_classes = (ScopedRateThrottle,)
    
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = 'drone-list'
    
    filter_fields = ('name', 'drone_category', 'manufacturing_date', 'has_it_completed_missions')
    search_fields = ('^name',)
    ordering_fields = ('name','manufacturing_date')
    
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, 
        custompermission.IsCurrentUserOwnerOrReadOnly
    )
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
    
class DroneDetail(generics.RetrieveUpdateDestroyAPIView):
    throttle_scope = 'drones'
    throttle_classes = (ScopedRateThrottle,)    
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = 'drone-detail'
    
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, 
        custompermission.IsCurrentUserOwnerOrReadOnly
        )
    
class PilotList(generics.ListCreateAPIView):
    throttle_scope = 'pilots'
    throttle_classes = (ScopedRateThrottle,)
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = 'pilot-list'
    
    filter_fields = ('name', 'gender', 'reces_count')
    search_fields = ('^name',)
    ordering_fields = ('name', 'reces_count')
    
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    
class PilotDetail(generics.RetrieveUpdateDestroyAPIView):
    throttle_scope = 'pilots'
    throttle_classes = (ScopedRateThrottle,)
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = 'pilot-detail'
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    
    
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