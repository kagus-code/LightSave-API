from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import User,Appliance,CustomAppliance

class UserSerializer(serializers.ModelSerializer):

   class Meta:
        model = User
        fields = [ 'id', 'username','email','password']
        extra_kwargs = {'password': {'write_only': True}
        }
        
   def create(self, validated_data):
          password =validated_data.pop('password', None)
          instance =self.Meta.model(**validated_data)
          if password is not None:
             instance.set_password(password)
          instance.save()   
          return instance

class ApplianceSerializer(serializers.ModelSerializer):

   class Meta:
      model = Appliance
      fields = '__all__'

class CustomApplianceSerializer(serializers.ModelSerializer):


   class Meta:
      model = CustomAppliance
      fields = '__all__'



