from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(UserTableDB)
admin.site.register(ContactUs)
admin.site.register(Subscription)