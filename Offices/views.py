from django.contrib.postgres.search import SearchVector
from django.db.models import Q
from rest_framework import generics, permissions, status
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.decorators import permission_classes
from rest_framework.views import APIView
from .serializers import *

@permission_classes((permissions.AllowAny,))
class State(generics.ListCreateAPIView):
    queryset = States.objects.all()
    serializer_class = StateSerializer

@permission_classes((permissions.AllowAny,))
class Search_Properties1(APIView):
    def post(self,request):
        data=request.data['keyword']
        status=request.data['type']
        try:
            page = int(request.GET.get('page'))
            if page < 1:
                page = 1
        except:
            page = 1
        print('oage>>>>>>>>>>>',page)
        item = page * 20
        offset = (page - 1) * 20
        results = property_detail.objects.annotate(search=SearchVector('country','address','state', 'city','zipcode','country')).filter(Q(search=data)&Q(post_type=status)).exclude(latitude=0).order_by('-posted_date')[offset:item]
        items = property_detail.objects.annotate(search=SearchVector('country','address','state', 'city','zipcode')).filter(Q(search=data)&Q(post_type=status)).exclude(latitude=0).count()
        pages = int(items / 20)
        if (items % 20) != 0:
             pages += 1
        serializer = Property_Search_Serializer(results, many=True)
        res={
            "totalpages": pages,
            "totalItems" : items,
            "results" : serializer.data
        }
        return Response(res)
@permission_classes((permissions.AllowAny,))
class Filter_Properties1(APIView):
    def post(self,request):
        try:
            # key = request.data['keyword']
            keyword=request.data
            q1= Q()
            if 'post_type' in keyword:
                q1 &= Q(post_type=request.data['post_type'])
            if 'property_type' in keyword:
                q1 &= Q(property_type=request.data['property_type'])
            if 'pricelowlimit'  and 'pricehighlimit' in keyword:
                q1 &= Q(price__gte=request.data['pricelowlimit'], price__lte=request.data['pricehighlimit'])
            if 'spacelowlimit'  and 'spacehighlimit' in keyword:
                q1 &= Q(property_area__gte=float(request.data['spacelowlimit']), property_area__lte=float(request.data['spacehighlimit']))

            try:
                page = request.GET.get('page')
                if page < 1:
                    page = 1
            except:
                page = 1
            item = page * 20
            offset = (page - 1) * 20
            if 'keyword' in keyword:
                key = request.data['keyword']
                results=property_detail.objects.annotate(keyword=SearchVector('country','address', 'city','zipcode','state',)).filter(Q(keyword=key)&q1).exclude(latitude=0).order_by('-posted_date')[offset:item]
                items=property_detail.objects.annotate(search=SearchVector('country','address', 'city','zipcode','state')).filter(Q(search=key)&q1).exclude(latitude=0).count()
            else:
                results = property_detail.objects.filter(q1).exclude(latitude=0).order_by('-posted_date')[offset:item]
                items = property_detail.objects.filter( q1).exclude(latitude=0).count()

            pages = int(items / 20)
            if (items % 20) != 0:
                pages += 1
            Serializer = Property_Search_Serializer(results, many=True)
            res = {
                'totalItems': items,
                'totalPages': pages,
                'Results': Serializer.data
            }
            return Response(res)

        except property_detail.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        pass
@permission_classes((permissions.AllowAny,))
class Property_Detail_By_Id(APIView):
    def get(self,request,pk):
        property = get_object_or_404(property_detail, pk=pk)
        serializer=Property_Search_Serializer1(property)
        li=[serializer.data]
        res={
            "results":li

        }

        return Response(res,status.HTTP_200_OK)


@permission_classes((permissions.AllowAny,))
class SimilarProperties(APIView):

    def get(self, request,pk):
        property=get_object_or_404(property_detail, pk=pk)
        similar_properties=property_detail.objects.filter(property_type=property.property_type,state=property.state,city=property.city,post_type=property.post_type).exclude(pk=pk)[:10]
        serializer=Property_Search_Serializer(similar_properties,many=True)
        return Response(serializer.data)

@permission_classes((permissions.AllowAny,))
class State_Properties(APIView):

    def get(self, request,state):
        print(state)
        try:
            page = int(request.GET.get('page'))
            if page < 1:
                page = 1
        except:
            page = 1
        item = page * 20
        offset = (page - 1) * 20
        print(item)
        print(offset)
        properties=property_detail.objects.filter(state=state)[offset:item]
        items = property_detail.objects.filter(state=str(state)).count()
        pages = int(items / 20)
        if (items % 20) != 0:
            pages += 1
        print(properties)
        serializer=Property_Search_Serializer(properties,many=True)
        res = {
            'totalItems': items,
            'totalPages': pages,
            'Results': serializer.data
        }
        return Response(res,status.HTTP_200_OK)
class LargeResultsSetPagination(LimitOffsetPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100
@permission_classes((permissions.AllowAny,))
class Listing_Services(generics.ListAPIView):
    queryset = Services.objects.all()
    serializer_class = Listing_Services_Serializer
    pagination_class = LargeResultsSetPagination

class Add_Listing(APIView):
    def post(self,request):
        address = request.data['address']
        property_title=request.data['property_title']
        latitude = request.data['latitude']
        longitude = request.data['longitude']
        property_type = request.data['property_type']
        pic_url= request.data['pic_url']

        description = request.data['description']
        price = request.data['price']
        price_type = request.data['price_type']
        presented_company= request.data['presented_company']
        presented_name= request.data['presented_name']
        state= request.data['state']
        zipcode= request.data['zipcode']
        city = request.data['city']
        services  =request.data['services']
        contact_no= request.data['contact_no']
        property_area = request.data['property_area']
        overview = request.data['overview']
        post_type=request.data['post_type']
        pics=''
        service=''
        i=0
        for pic in pic_url:
            if i==0:
                pics=pic
                one_pic=pics
                i=1
            else:
                pics=pics+",,,"+pic
        i = 0
        for serve in services:
            if i==0:
                service=serve
                i=1
            else:
                service = service + ",,,"+serve

        obj=property_detail(user = request.user,address=address,latitude=latitude,longitude=longitude,property_type=property_type,\
                            pic_url=pics,one_pic=one_pic,description=description,price=price,price_type=price_type,presented_company=presented_company,\
                            presented_name=presented_name,state=state,zipcode=zipcode,city=city,services=service,contact_no=contact_no,\
                            property_area=property_area,overview=overview, property_title= property_title,post_type=post_type)
        obj.save()

        return Response("Accepted",status.HTTP_200_OK)

class User_Properties(APIView):
    def get(self,request):
        user_properties=property_detail.objects.filter(property_area=None).count()
        print(user_properties)
        serializer=User_Property_Serializer(user_properties,many=True)
        return Response({'Results':serializer.data},status.HTTP_200_OK)

class Get_Put_Del_Property(generics.RetrieveUpdateDestroyAPIView):
    queryset=property_detail.objects.all()
    serializer_class=Get_Put_Del_Property_Serializer

class User_Favourite(APIView):
    def post(self,request,pk):
        user=request.user
        property=property_detail.objects.get(id=pk)
        if User_Favourites.objects.filter(user=user,Property_id=pk).exists():
            return Response({"results":"Already Exist"},status.HTTP_201_CREATED)
        else:
            obj=User_Favourites(user=user,Property_id=property)
            obj.save()
            return Response({"results":"Added"},status.HTTP_200_OK)

class Get_User_Favourite(APIView):
    def get(self,request):
        user_properties=User_Favourites.objects.filter(user=request.user)
        serializer=User_FavouriteSerializer(user_properties, many=True)
        return Response({"rersults" :serializer.data},status.HTTP_200_OK)

class Delete_User_Favourite(generics.DestroyAPIView):
    queryset = User_Favourites.objects.all()
    serializer_class = Delete_User_Serializer

@permission_classes((permissions.AllowAny,))
class PropertyType(APIView):
    def get(self,request):
        obj=Property_Type.objects.all().values('id','Property_type')
        return Response(obj)

# class SpaceType(APIView):
#     def get(self,request):
#         obj=property_detail.objects.all().distinct('property_type')
#         for data in obj:
#             property_type=Property_Type(Property_type=data.property_type)
#             property_type.save()
#         return Response("saved")

# class SpaceType(APIView):
#     def get(self,request):
#         obj=property_detail.objects.filter(post_type='buy')
#         i=1
#         for data in obj:
#             data.delete()
#             # data.property_type="Office Medical Retail "
#             # data.save()
#             # print(i,data.property_type)
#             i+=1
#         return Response("ok")

class SpaceType(APIView):
    def get(self,request):
        obj=property_detail.objects.filter(user=request.user).count()
        # for data in obj:
        #     data.delete()
        #     print('deleted')
        return Response(obj)

