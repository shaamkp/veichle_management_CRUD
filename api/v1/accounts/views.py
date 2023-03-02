import requests

from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.permissions import AllowAny

from accounts.models import AdminProfile, SuperAdminProfile, UserProfile
from api.v1.accounts.serializers import AdminProfileSerializer, SuperAdminProfileSerializer, UserProfileSerializer
from general.functions import generate_serializer_errors
from general.encryption import encrypt, decrypt



@api_view(['POST'])
@permission_classes([AllowAny])
def login_user_profile(request):
    serialized = UserProfileSerializer(data=request.data)
    if serialized.is_valid():
        # Getting login details
        username = request.data.get('username')
        password = request.data.get('password')

        if UserProfile.objects.filter(username=username, is_deleted=False).exists():
            profile = UserProfile.objects.get(username=username, is_deleted=False)

            if decrypt(profile.password) == password:

                protocol = "http://" 
                if request.is_secure():
                    protocol = "https://"

                web_host = request.get_host()
                request_url = protocol + web_host + "/api/v1/accounts/token/"

                login_response = requests.post(
                    request_url,
                    data={
                        'username': profile.user.username,
                        'password': password,
                    }
                )

                if login_response.status_code == 200:
                    login_response = login_response.json()

                    active_roles = []
                    current_roles = profile.user.groups.all()
                    for role in current_roles:
                        active_roles.append(role.name)

                    response_data = {
                        "StatusCode": 6000,
                        "data" : {
                            "title": "Success!",
                            "message": "Success!",
                            "access_token": login_response["access"],
                            "refresh_token": login_response["refresh"],
                            "roles": active_roles,
                        },
                    }
                else:
                    response_data = {
                        "StatusCode": 6001,
                        "data" : {
                            "title": "Failed!",
                            "message": "Token generation failed",
                            "login_status_code" :  login_response.status_code
                        },
                    }
            else:
                response_data = {
                    "StatusCode": 6001,
                    "data" : {
                        "title": "Failed",
                        "message": "Password is incorrect",
                    },
                }
        else:
            response_data = {
                "StatusCode": 6001,
                "data" : {
                    "title": "Failed",
                    "message": "User Not Exists"
                },
            }
    else:
        response_data = {
            "StatusCode": 6001,
            "data": {
                "title": "Validation Error",
                "message": generate_serializer_errors(serialized._errors)
            }
        }
    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def login_admin_profile(request):
    serialized = AdminProfileSerializer(data=request.data)
    if serialized.is_valid():
        # Getting login details
        username = request.data.get('username')
        password = request.data.get('password')

        if AdminProfile.objects.filter(username=username, is_deleted=False).exists():
            profile = AdminProfile.objects.get(username=username, is_deleted=False)

            if decrypt(profile.password) == password:

                protocol = "http://" 
                if request.is_secure():
                    protocol = "https://"

                web_host = request.get_host()
                request_url = protocol + web_host + "/api/v1/accounts/token/"

                login_response = requests.post(
                    request_url,
                    data={
                        'username': profile.user.username,
                        'password': password,
                    }
                )

                if login_response.status_code == 200:
                    login_response = login_response.json()

                    active_roles = []
                    current_roles = profile.user.groups.all()
                    for role in current_roles:
                        active_roles.append(role.name)

                    response_data = {
                        "StatusCode": 6000,
                        "data" : {
                            "title": "Success!",
                            "message": "Success!",
                            "access_token": login_response["access"],
                            "refresh_token": login_response["refresh"],
                            "roles": active_roles,
                        },
                    }
                else:
                    response_data = {
                        "StatusCode": 6001,
                        "data" : {
                            "title": "Failed!",
                            "message": "Token generation failed",
                            "login_status_code" :  login_response.status_code
                        },
                    }
            else:
                response_data = {
                    "StatusCode": 6001,
                    "data" : {
                        "title": "Failed",
                        "message": "Password is incorrect",
                    },
                }
        else:
            response_data = {
                "StatusCode": 6001,
                "data" : {
                    "title": "Failed",
                    "message": "User Not Exists"
                },
            }
    else:
        response_data = {
            "StatusCode": 6001,
            "data": {
                "title": "Validation Error",
                "message": generate_serializer_errors(serialized._errors)
            }
        }
    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def login_super_admin_profile(request):
    serialized = SuperAdminProfileSerializer(data=request.data)
    if serialized.is_valid():
        # Getting login details
        username = request.data.get('username')
        password = request.data.get('password')

        if SuperAdminProfile.objects.filter(username=username, is_deleted=False).exists():
            profile = SuperAdminProfile.objects.get(username=username, is_deleted=False)

            if decrypt(profile.password) == password:

                protocol = "http://" 
                if request.is_secure():
                    protocol = "https://"

                web_host = request.get_host()
                request_url = protocol + web_host + "/api/v1/accounts/token/"

                login_response = requests.post(
                    request_url,
                    data={
                        'username': profile.user.username,
                        'password': password,
                    }
                )

                if login_response.status_code == 200:
                    login_response = login_response.json()

                    active_roles = []
                    current_roles = profile.user.groups.all()
                    for role in current_roles:
                        active_roles.append(role.name)

                    response_data = {
                        "StatusCode": 6000,
                        "data" : {
                            "title": "Success!",
                            "message": "Success!",
                            "access_token": login_response["access"],
                            "refresh_token": login_response["refresh"],
                            "roles": active_roles,
                        },
                    }
                else:
                    response_data = {
                        "StatusCode": 6001,
                        "data" : {
                            "title": "Failed!",
                            "message": "Token generation failed",
                            "login_status_code" :  login_response.status_code
                        },
                    }
            else:
                response_data = {
                    "StatusCode": 6001,
                    "data" : {
                        "title": "Failed",
                        "message": "Password is incorrect",
                    },
                }
        else:
            response_data = {
                "StatusCode": 6001,
                "data" : {
                    "title": "Failed",
                    "message": "User Not Exists"
                },
            }
    else:
        response_data = {
            "StatusCode": 6001,
            "data": {
                "title": "Validation Error",
                "message": generate_serializer_errors(serialized._errors)
            }
        }
    return Response(response_data, status=status.HTTP_200_OK)