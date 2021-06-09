
from django.core.checks import messages
from django.http import response
from lightsave.models import User,Appliance,CustomAppliance
from rest_framework import serializers,status
from lightsave.serializers import UserSerializer,ApplianceSerializer,CustomApplianceSerializer
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from rest_framework.response import Response
import jwt, datetime
from rest_framework import generics
from rest_framework import filters
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse


# Create your views here.
class RegisterApiView(APIView):
  def post(self, request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      user_data =serializer.data
      response={
        "data":{
            "user":dict(user_data),
            "status":"success",
            "message":"user added successfully",
        }
      }
      return Response(response, status=status.HTTP_201_CREATED)
    else:
      return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginApiView(APIView):
  def post(self, request):
    email = request.data['email']
    password =request.data['password']

    user = User.objects.filter(email=email).first()
    if user is None:
      raise AuthenticationFailed("User not Found")


    if not user.check_password(password):
      raise AuthenticationFailed("incorrect password ")  

    payload = {
      'id':user.id,
      'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
      'iat': datetime.datetime.utcnow()
    }  
    token = jwt.encode(payload, 'secret', algorithm='HS256')


    response = Response()  
    response.set_cookie(key='jwt',value=token,httponly=True)
    response.data = {"jwt": token}

    return response

class UserAPIView(APIView):

  def get(self, request):
    token = request.COOKIES.get('jwt')
    
    if not token:
      raise AuthenticationFailed("Unauthenticated")

    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    except jwt.ExpiredSignatureError:  
      raise AuthenticationFailed("Unauthenticated")

    user = User.objects.filter(id=payload['id']).first()
    serializer = UserSerializer(user)
  
    return Response(serializer.data)

class LogoutAPIView(APIView):
  def post(self, request):
    response = Response()
    response.delete_cookie('jwt')
    response.data = {"message":"successfully logged out"}

    return response

class ApplianceApiView(APIView):
  serializer_class = ApplianceSerializer
  def get(self,request,format=None):
    all_appliances = Appliance.objects.all()
    serializers =ApplianceSerializer(all_appliances,many=True)
    return Response (serializers.data)

class SearchAppliance(generics.ListCreateAPIView):
  search_fields =['name']
  filter_backends = (filters.SearchFilter,)
  queryset = Appliance.objects.all()
  serializer_class = ApplianceSerializer


class CustomApplianceView(APIView):
  serializer_class = CustomApplianceSerializer
  def get(self,request,format=None):
    all_customs= CustomAppliance.objects.all()
    serializers= CustomApplianceSerializer(all_customs,many=True)
    return Response (serializers.data)

  def post(self,request):
    serializer =self.serializer_class(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save()
      customApp_data =serializer.data
      response={
        "data":{
            "Custom-Appliance":dict(customApp_data),
            "status":"success",
            "message":"Custom Appliance added successfully",
        }
      }
      return Response(response, status=status.HTTP_201_CREATED)
    else:
      return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

  def put(self,request,format=None):
    custom_data =JSONParser().parse(request)
    customApp=CustomAppliance.objects.get(appliaceId=custom_data['applianceId'])
    customApp_serializer = CustomApplianceSerializer(customApp,data=custom_data)
    if customApp_serializer.is_valid():
      customApp_serializer.save()
      return Response(customApp_serializer.data)
    else:
      return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST) 

  def delete(self,request,format=None):
    custom_data =JSONParser().parse(request)
    customApp=CustomAppliance.objects.get(appliaceId=custom_data['applianceId'])
    customApp.delete()
    return JsonResponse("Delete successfull",safe=False)


  