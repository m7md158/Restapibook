from rest_framework import serializers
from .models import Pilot, Drone, Competition, DroneCategory
import drones.views

class DroneCategorySerializer(serializers.HyperlinkedModelSerializer):
    drones = serializers.HyperlinkedRelatedField(
        many = True,
        read_only = True,
        view_name = 'drone-detail'
    )
    class Meta:
        model = DroneCategory
        fields = ['url', 'pk', 'name', 'drones']
        
        
        
class DroneSerializer(serializers.HyperlinkedModelSerializer):
    drone_category = serializers.SlugRelatedField(
        queryset=DroneCategory.objects.all(),slug_field='name'
        
    )
    
    class Meta:
        model = Drone
        fields = ['url', 'name', 'inserted_timestamp','drone_category', 'manufacturing_date', 'has_it_completed_missions']
        
        
class CompetitionSerializer(serializers.HyperlinkedModelSerializer):
    
    drone = DroneSerializer()
    
    class Meta:
        model = Competition
        fields = ['url', 'pk', 'drone', 'distance_in_feet', 'distance_achievement_date']

class PilotSerializer(serializers.HyperlinkedModelSerializer):
    competitions = CompetitionSerializer(many=True, read_only=True)
    gender = serializers.ChoiceField(choices=Pilot.GENDER_CHOICES)
    gender_description = serializers.CharField(source= 'get_gender_display', read_only=True)
    
    class Meta:
        model = Pilot
        fields = ['url', 'name', 'gender', 'gender_description', 'reces_count', 'inserted_timestamp', 'competitions']
        

class PilotCompetitionSerializer(serializers.ModelSerializer):
    pilot = serializers.SlugRelatedField(queryset=Pilot.objects.all(),
    slug_field='name')
    # Display the drone's name
    drone = serializers.SlugRelatedField(queryset=Drone.objects.all(),
    slug_field='name')
    class Meta:
        model = Competition
        fields = (
        'url',
        'pk',
        'distance_in_feet',
        'distance_achievement_date',
        'pilot',
        'drone')