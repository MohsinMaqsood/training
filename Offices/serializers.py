from rest_framework import serializers
from .models import *
class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = States
        fields = '__all__'
class Property_Search_Serializer(serializers.ModelSerializer):
    class Meta:
        model = property_detail
        fields = ('id','property_title','property_type','one_pic', 'price', 'property_area', 'address', 'post_type','latitude','longitude')
class Property_Search_Serializer1(serializers.ModelSerializer):
    class Meta:
        model = property_detail
        fields = '__all__'

class Listing_Services_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'

class Add_Listing_Serializer(serializers.ModelSerializer):
    class Meta:
        model = property_detail
        fields = ('user','address','latitude','longitude','property_type','pic_url','one_pic','description','price','price_type',\
                  'presented_company','presented_name','state','zipcode','city','services','contact_no','property_area','overview')
class User_Property_Serializer(serializers.ModelSerializer):
    class Meta:
        model = property_detail
        fields = '__all__'

class Get_Put_Del_Property_Serializer(serializers.ModelSerializer):
    class Meta:
        model=property_detail
        fields=('user', 'address', 'latitude', 'longitude', 'property_type', 'pic_url', 'one_pic', 'description', 'price', 'price_type', \
     'presented_company', 'presented_name', 'state', 'zipcode', 'city', 'services', 'contact_no', 'property_area', 'overview')

class User_FavouriteSerializer(serializers.ModelSerializer):
    Property_id = Property_Search_Serializer()
    class Meta:
        model = User_Favourites
        fields = '__all__'

class Delete_User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User_Favourites
        fields = '__all__'