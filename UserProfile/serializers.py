from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
# ...
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from.views import *



class UserSerializer1(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validated_data):
            user = User.objects.create_user(
                email=validated_data['email'],
                username=validated_data['username'],
                password=validated_data['password']
            )

            # user.set_password(make_password(validated_data['password']))
            user.save()
            return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model =User
        fields=('username','email','id','first_name','last_name',)

class UserTableDBSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model =UserTableDB
        fields = ('Fname','Lname','Mobile','user','Country','State','City','Address','ISActive','Pic')

class UserTableUpdateDBSerializer(serializers.ModelSerializer):
    class Meta:
        model =UserTableDB
        fields = ('Fname','Lname','Mobile','Country','State','City','Address','Zip','Pic')

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model=ContactUs
        fields='__all__'
