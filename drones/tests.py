from django.test import TestCase
from django.utils.http import urlencode
from django.urls import reverse
from rest_framework import status

from rest_framework.test import APITestCase
from drones.models import DroneCategory, Pilot
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from drones import views


class DroneCategoryTest(APITestCase):
    def post_drone_category(self,name):
        url = reverse(views.DroneCategoryList.name)
        data = {'name': name}
        response = self.client.post(url, data, format='json')
        return response
    
    def test_post_and_get_drone_category(self):
        new_drone_category_name = 'Hexacopter'
        response = self.post_drone_category(new_drone_category_name)
        assert response.status_code == status.HTTP_201_CREATED
        assert DroneCategory.objects.count() == 1
        assert DroneCategory.objects.get().name == new_drone_category_name
        
    def test_post_existing_drone_category_name(self):
        name = 'Duplicateed Copter'
        self.post_drone_category(name)
        response = self.post_drone_category(name)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        
        
    def test_filter_drone_category_by_name(self):
        name1 = 'Hexacopter'
        name2 = 'Octocopter'
        self.post_drone_category(name1)
        self.post_drone_category(name2)
        url = f"{reverse(views.DroneCategoryList.name)}?{urlencode({'name': name1})}"
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        assert response.data['results'][0]['name'] == name1

    def test_get_drone_categories_collection(self):
        name = 'Super Copter'
        self.post_drone_category(name)
        url = reverse(views.DroneCategoryList.name)
        response = self.client.get(url, format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 1
        
    def test_update_drone_category(self):
        name = 'Initial Name'
        response = self.post_drone_category(name)
        url = reverse(views.DroneCategoryDetail.name, kwargs={'pk': response.data['pk']})
        data = {'name': 'Updated Name'}
        patch_response = self.client.patch(url, data, format='json')
        assert patch_response.status_code == status.HTTP_200_OK
        assert patch_response.data['name'] == 'Updated Name'
        
    def test_get_drone_category(self):
        name = 'Easy to retrieve'
        response = self.post_drone_category(name)
        url = reverse(views.DroneCategoryDetail.name, kwargs={'pk': response.data['pk']})
        get_response = self.client.get(url, format='json')
        assert get_response.status_code == status.HTTP_200_OK
        assert get_response.data['name'] == name


class PilotTest(APITestCase):
    def post_pilot(self,name, gender, reces_count):
        url = reverse(views.PilotList.name)
        data = {
            'name': name,
            'gender': gender,
            'reces_count': reces_count
        }
        response = self.client.post(url, data, format='json')
        return response
    
    def create_user_and_set_token_credentials(self):
        user = User.objects.create_user(username='user01',email='user01@example.com' ,password='user01P4ssw0rD')
        token = Token.objects.create(user=user)
        self.client.credentials(HTTP_AUTHORIZATION='Token {0}'.format(token.key))
    
    
    def test_post_and_get_pilot(self):
        self.create_user_and_set_token_credentials()

        # create new pilot
        response = self.post_pilot('Gaston', Pilot.MALE, 5)
        assert response.status_code == status.HTTP_201_CREATED
        assert Pilot.objects.count() == 1

        saved_pilot = Pilot.objects.get()
        assert saved_pilot.name == 'Gaston'
        
        
        # Get Token
        url = reverse(views.PilotDetail.name, None, {saved_pilot.pk})
        authorized_get_response = self.client.get(url, format='json')
        assert authorized_get_response.status_code == status.HTTP_200_OK

        #  Unauthorized
        self.client.credentials()
        unauthorized_get_response = self.client.get(url, format='json')
        assert unauthorized_get_response.status_code == status.HTTP_401_UNAUTHORIZED
        
    def test_try_to_post_pilot_without_token(self):
        response = self.post_pilot('Unauthorized Pilot', Pilot.MALE, 5)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
        assert Pilot.objects.count() == 0
