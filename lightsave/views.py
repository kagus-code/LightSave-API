
from django.core.checks import messages
from lightsave.models import User
from rest_framework import serializers,status
from lightsave.serializers import UserSerializer
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from rest_framework.response import Response


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

    return Response({"message": "success"})  

