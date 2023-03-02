

from api.v1.web.serialzers import AddVeichleDetailsSerializer, ViewVeichleSerializer
from general.functions import generate_serializer_errors
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from general.decorators import group_required
from web.models import VeichleDetails

@api_view(['GET'])
@group_required(['super_admin','admin', 'user'])
def veichle_details(request):
    if (veichle_details:=VeichleDetails.objects.filter(is_deleted=False)).exists(): #will reduce the database hit

        serialized_data = ViewVeichleSerializer(
            veichle_details,
            many=True,
            context = {
                "request" : request
            }
        ).data

        response_data = {
            "StatusCode" : 6000,
            "data" : {
                "title" : "Success",
                "data" : serialized_data
            }
        }
    else:
        response_data = {
            "StatusCode" : 6001,
            "data" : {
                "title" : "Failed",
                "message" : "Veichle Details not found"
            }
        }
    
    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['POST'])
@group_required(['super_admin'])
def add_veichle_details(request):
    serialized_data = AddVeichleDetailsSerializer(data=request.data)

    if serialized_data.is_valid():
        number = request.data['number']
        veichle_type = request.data['veichle_type']
        model = request.data['model']
        description = request.data['description']

        if not VeichleDetails.objects.filter(number=number, is_deleted=False).exists():

            veichle_details = VeichleDetails.objects.create(
                number = number,
                veichle_type = veichle_type,
                model = model,
                description = description
            )

            response_data = {
                "StatusCode" : 6000,
                "Data" : {
                    "title" : "Success",
                    "message" : "Veichle added succesfully"
                }
            }
        else:
            response_data = {
                "StatusCode" : 6001,
                "data" : {
                    "title" : "Failed",
                    "message" : "Veichle is already exists"
                }
            }
    else:
        response_data = {
            "StatusCode": 6001,
            "data": {
                "title": "Validation Error",
                "message": generate_serializer_errors(serialized_data._errors)
            }
        }

    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['POST'])
@group_required(['super_admin', 'admin'])
def edit_veichle_details(request,pk):
    number = request.data.get('number')
    veichle_type = request.data.get('veichle_type')
    model = request.data.get('model')
    description = request.data.get('description')

    if (veichle_details:=VeichleDetails.objects.filter(id=pk, is_deleted=False)).exists(): #will reduce the database hit
        veichle_details = veichle_details.latest('id')

        if number:
            veichle_details.number = number
        if veichle_type:
            veichle_details.veichle_type = veichle_type
        if model:
            veichle_details.model = model
        if description:
            veichle_details.description = description

        veichle_details.save()

        response_data = {
            "StatusCode" : 6000,
            "Data" : {
                "title" : "Success",
                "message" : "Veichle edit succesfully completed"
            }
        }
    else:
        response_data = {
            "StatusCode" : 6001,
            "data" : {
                "title" : "Failed",
                "message" : "Veichle details not found"
            }
        }


    return Response(response_data, status=status.HTTP_200_OK)


@api_view(['POST'])
@group_required(['super_admin'])
def delete_veichle_details(request,pk):
    if (veichle_details:=VeichleDetails.objects.filter(id=pk, is_deleted=False)).exists(): #will reduce the database hit
        veichle_details = veichle_details.update(is_deleted=True)

        response_data = {
            "StatusCode" : 6000,
            "Data" : {
                "title" : "Success",
                "message" : "Veichle details succesfully deleted"
            }
        }
    else:
        response_data = {
            "StatusCode" : 6001,
            "data" : {
                "title" : "Failed",
                "message" : "Veichle details not found"
            }
        }


    return Response(response_data, status=status.HTTP_200_OK)


