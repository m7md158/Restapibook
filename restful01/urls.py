"""
URL configuration for restful01 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include


# urlpatterns = [
#     path('v1/', include(('drones.urls', 'drones'), namespace='v1')),
#     path('v1/api-auth/', include(('rest_framework.urls', 'rest_framework'), namespace='rest_framework_v1')),

#     path('v2/', include(('drones.v2.urls', 'drones_v2'), namespace='v2')),
#     path('v2/api-auth/', include(('rest_framework.urls', 'rest_framework'), namespace='rest_framework_v2')),
# ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('drones.urls')),
    path('api-auth/', include('rest_framework.urls')),

]
