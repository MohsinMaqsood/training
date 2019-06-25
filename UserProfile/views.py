# in apiviews.py
from django.contrib.auth.models import User
from rest_framework import generics
import random
import string
from rest_framework.decorators import permission_classes, api_view
from rest_framework.response import Response
from rest_framework.views import APIView
import after_response
from .models import *
from django.core.mail.message import EmailMessage
from django.template.loader import get_template
from .serializers import UserSerializer
from rest_framework import status, permissions
from .serializers import *

@after_response.enable
def emailsending(key,template,email,msg):
    print('ok')
    message = get_template(template).render(key)
    email = EmailMessage(msg, message, to=[email])
    email.content_subtype = 'html'
    email.send()
    print('Email Snd Successfully')



@permission_classes((permissions.AllowAny,))
class UserCreate(APIView):
    def post(self, request,):
        user = User(
            email=request.data['email'],
            username=request.data['username'],
            # password=request.data['password']
        )
        user.set_password(request.data['password'])
        user.save()
        if user !='':
            print('ok')
            user=User.objects.get(username=request.data['username'])
            print('ok')
            secret_id = ''.join(
                random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(200))
            key = {
                'link': 'https://www.ogrespace.com/login/' + secret_id,
                'username':request.data['fname'],
                #'link': 'http://192.168.30.225:7000/VerfiyEmail/' + secret_id
            }
            print(secret_id)
            _Register = UserTableDB(
                user=user,
                Fname=request.data['fname'],
                Lname=request.data['lname'],
                Mobile=request.data['mobile'],
                Country=request.data['country'],
                State=request.data['state'],
                City=request.data['city'],
                Zip=request.data['zip'],
                Address=request.data['address'],
                Pic=request.data['pic'],
                Activation_Key=secret_id
            )
            _Register.save()
            emailsending.after_response(key,'Activation_Email.html',user.email,'Email Confirmation')
            return Response({"message":"Account Successfully Created"},status.HTTP_200_OK)

# class EmailExist(APIView):
#     def post


class LoginChangePassword(APIView):
    def post(self,request):
        user = User.objects.get(username=request.user.username)
        success = (user.check_password(request.data['currentPassword']))
        print("Success", success)
        if success == True:
            if request.data['newPassword'] == request.data['newPassword2']:
                # obj.password = request.data['newPassword']
                user.set_password(request.data['newPassword'])
                print("User", user.password)
                user.save()
                key={
                    'username':request.user.username,
                    'oldpassword':request.data['currentPassword'],
                    'newpassword':request.data['newPassword']
                }
                emailsending.after_response(key, 'Change_Password.html', user.email, 'Change_Password')
                return Response({"message":"Your Password has been Successfully changed"}, status=status.HTTP_200_OK)
            else:
                return Response({"message":"Password Not Match"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message":"Incorrect Password"}, status=status.HTTP_400_BAD_REQUEST)


@permission_classes((permissions.AllowAny,))
class EmailVerify(APIView):
    def post(self, request):
        email=request.data['email']
        if User.objects.filter(email=email).exists():
            return Response({"message":"Email Already Exist"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Email Available"}, status=status.HTTP_200_OK)


@permission_classes((permissions.AllowAny,))
class UsernameVerify(APIView):
    def post(self, request):
        username=request.data['username']
        if User.objects.filter(username=username).exists():
            return Response({"message":"Username Already Exist"}, status=status.HTTP_200_OK)
        else:
            return Response({"message": "Username Available"}, status=status.HTTP_200_OK)


@permission_classes((permissions.AllowAny,))
class ForgetPssword(APIView):
    def post(self, request):
        email = request.data['email']
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            reg_obj = UserTableDB.objects.get(user= user)
            if (reg_obj.ISConfirmed == True):
                reset_email_token = ''.join(
                    random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _
                    in range(200))
                while (UserTableDB.objects.filter(Activation_Key=reset_email_token).exists()):
                    reset_email_token = ''.join(
                        random.SystemRandom().choice(string.ascii_uppercase + string.digits + string.ascii_lowercase)
                        for _
                        in
                        range(100))
                key = {
                    'link': 'https://www.ogrespace.com/reset/' +str(user.id)+'/'+ reset_email_token,
                    'username':user.username
                }
                emailsending.after_response(key,'reset_email.html',user.email,'Password Reset')
                reg_obj.Activation_Key = reset_email_token
                reg_obj.save()
                return Response({'message':'Reset Password mail send Successfully'},status.HTTP_200_OK)
            else:
                return Response({'message':'User Not verify'},status.HTTP_200_OK)
        else:
            return Response({'message': 'Email Not Exist'}, status.HTTP_200_OK)


@permission_classes((permissions.AllowAny,))
class ResetPssword(APIView):
    def post(self, request):
        activition_key = request.data['activation_key']
        password= request.data['password']
        if(UserTableDB.objects.filter(Activation_Key=activition_key).exists()):
            customer = UserTableDB.objects.get(Activation_Key=activition_key)
            user= User.objects.get(email=customer.user.email)
            user.set_password(password)
            user.save()
            return Response({'message':'Password Reset Successfully'},status.HTTP_202_ACCEPTED)

@permission_classes((permissions.AllowAny,))
class ActivateAccount(APIView):
    def post(self, request):
        key=request.data['activation_key']
        obj_= UserTableDB.objects.get(Activation_Key=key)
        obj_.ISConfirmed = True
        obj_.save()
        key={
            'username':obj_.Fname
        }
        emailsending.after_response(key, 'Registration.html', obj_.user.email, 'Password Reset')
        return Response({'message':'Successfully Activated'},status=status.HTTP_202_ACCEPTED)

@permission_classes((permissions.AllowAny,))
class IsActive(APIView):
    def post(self, request):
        try:
            user = User.objects.get(username=request.data['username'])
        except:
            return Response({'message': "Username does not exist"}, status=status.HTTP_404_NOT_FOUND)
        reg_obj = UserTableDB.objects.get(user=user)
        if (reg_obj.ISConfirmed == True):
            return Response({'message': 'Activated', 'status': True}, status=status.HTTP_202_ACCEPTED)
        else:

            return Response({'message': 'Not Activated', 'status': False}, status=status.HTTP_404_NOT_FOUND)


class GetUserDetail(APIView):
    def get(self, request):
        queryset = UserTableDB.objects.filter(user=request.user)
        serializer_class = UserTableDBSerializer(queryset,many=True)
        return Response(serializer_class.data,status.HTTP_200_OK)


class UpdateProfile(generics.UpdateAPIView):
    queryset = UserTableDB.objects.all()
    serializer_class = UserTableUpdateDBSerializer

@permission_classes((permissions.AllowAny,))
class Contact_US(APIView):
    def post(self,request):
        Message = ContactUs(
            Name=request.data['Name'],
            Email=request.data['Email'],
            CompanyName=request.data['CompanyName'],
            Telephone=request.data['Telephone'],
            Message=request.data['Message'], )
        key = {
            'name': Message.Name,
            'Email': Message.Email,
            'Telephone': Message.Telephone
        }
        emailsending.after_response(key, 'contact_us.html', Message.Email, 'Change_Password')
        Message.save()

        return Response(Message,status.HTTP_200_OK)
@permission_classes((permissions.AllowAny,))
class Subscribe(APIView):
    def post(self,request):
        email = request.data['email']
        emailcheck = Subscription.objects.filter(Email=email).exists()
        if emailcheck == True:
            return Response({'MESSAGE': 'ALREADY EXISTS..!!!'}, status.HTTP_200_OK)
        else:
            len = Subscription(Email=email)
            len.save()
            key = {
                'email' : email,
            }
            emailsending.after_response(key, 'subscrribe.html', email, 'Change_Password')
        return Response({'MESSAGE': 'SUCCESSFULLY SUBSCRIBED...!!!'}, status.HTTP_200_OK)

class UserProfile(APIView):
    def get(self,request,pk):
        username = User.objects.filter(pk=pk).values('id','username')
        userprofile=UserTableDB.objects.filter(user=pk).values('Fname','Lname','Country','State','City','Address','Zip','Pic')
        dic={
            "user_details":username,
            "user_profile": userprofile
        }
        return Response({"results":dic},status.HTTP_200_OK)



