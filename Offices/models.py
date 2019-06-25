from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
from django.db import models

class States(models.Model):
    state = models.CharField(max_length=100,null=True)
    icon_image=models.CharField(max_length=100,null=True)
    def __str__(self):
        return  self.state

# class Property_Type(models.Model):
#     type=models.CharField(max_length=255, blank=True,null=True)
#     def __str__(self):
#         return self.type
class property_detail(models.Model):
    user=models.ForeignKey(User, null=True, on_delete=models.CASCADE, blank=True,default=None)
    property_link = models.CharField(max_length=30000, null=True, blank=True)
    address = models.CharField(max_length=30000, null=True, blank=True)
    latitude = models.DecimalField(max_digits=25, null=True, blank=True, default=0.00,decimal_places=20)
    longitude = models.DecimalField(max_digits=25, null=True, blank=True, default=0.00,decimal_places=20)
    property_type = models.CharField(max_length=100, null=True, blank=True)
    pic_url = models.CharField(max_length=30000, null=True, blank=True)
    one_pic = models.CharField(max_length=30000, null=True, blank=True)
    property_id = models.CharField(max_length=1000, blank=True, null=True)
    description = models.CharField(max_length=30000, blank=True, null=True)
    price =models.DecimalField(max_digits=25, null=True, blank=True, default=0.00,decimal_places=2)
    presented_company = models.CharField(max_length=10000, null=True, blank=True)
    presented_name = models.CharField(max_length=10000, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    zipcode=models.CharField(max_length=25,null=True, blank=True)
    city = models.CharField(max_length=300, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    posted_date = models.CharField(max_length=100, null=True, blank=True)
    services = models.CharField(max_length=30000, null=True, blank=True)
    property_title = models.CharField(max_length=10000, null=True, blank=True)
    contact_no = models.CharField(max_length=10000, null=True, blank=True)
    active_bool = models.BooleanField(default=True,null=True)
    property_area = models.DecimalField(max_digits=25, null=True, blank=True, default=0.00,decimal_places=2)
    price_type = models.CharField(max_length=10000,null=True,blank=True)
    post_type = models.CharField(max_length=1000,null=True,blank=True)
    features = models.CharField(max_length=30000,null=True,blank=True)
    overview = models.CharField(max_length=30000,null=True,blank=True)
    overviewtag = models.CharField(max_length=30000, null=True, blank=True)
    destag=models.CharField(max_length=30000,null=True,blank=True)
    subspace_status=models.BooleanField(default=False,blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True,null=True)
    def __str__(self):
        return (self.property_title)


class property_subdetail(models.Model):
        propertylink = models.ForeignKey(property_detail, on_delete=models.CASCADE)
        sub_space_title = models.CharField(max_length=30000, null=True, blank=True)
        subspace_detail = models.CharField(max_length=30000, null=True, blank=True)
        subspace_detail_tag = models.CharField(max_length=30000, null=True, blank=True)
        subspace_pics = models.CharField(max_length=30000, null=True, blank=True)

        def __str__(self):
            return (self.sub_space_title)

class Services(models.Model):
    Service_Title=models.CharField(max_length=1000,null=True,blank=True)
    Property_Type=models.CharField(max_length=1000,null=True,blank=True)
    def __str__(self):
        return (self.Service_Title)

class User_Favourites(models.Model):
    user=models.ForeignKey(User, null=True, on_delete=models.CASCADE, blank=True,default=None)
    Property_id=models.ForeignKey(property_detail,null=True,on_delete=models.CASCADE,blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

class Property_Type(models.Model):

    Property_type=models.CharField(max_length=255,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
