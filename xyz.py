import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "OfficeDoor.settings")
django.setup()

# from
# from request import REQUEST
import requests
from urllib.request import urlopen


def picupload():
    my_url = 'https://storage.officedoor.ai/hamzatest.php'
    path1 = '/home/hassan/Downloads/states'
    print ('done')
    filename = os.listdir(path1)
    for f in filename:
        name=f[:-8]
        print(name)
        files = {'fileToUpload': open(path1, 'rb')}
        response = requests.request("POST", my_url, files=files)
        obj=States(state=name,icon_image=response.content)
        print(response.content)
        obj.save()
        break
        print ('ok')

# picupload()

# print(property_detail.objects.filter(price=""))
