from django.urls import path

from . import views
from .views import *
urlpatterns = [
# ...
path("createuser/", UserCreate.as_view(), name="user_create"),#signup user
path("EmailVerify/", EmailVerify.as_view(), name="EmailVerify"),#Email Verify
path("UsernameVerify/", UsernameVerify.as_view(), name="UsernameVerify"),#Username Verify
path("ForgetPssword/", ForgetPssword.as_view(), name="ForgetPssword"),#forget password
path("ResetPssword/", ResetPssword.as_view(), name="ResetPssword"),#reset password
path("ActivateAccount/", ActivateAccount.as_view(), name="ActivateAccount"),#Account Activation
path("IsActive/", IsActive.as_view(), name="IsActive"),#check account active or not
path("GetUserDetail/", GetUserDetail.as_view(), name="GetUserDetail"),#Get User Detail
path(r'user_change_password/',LoginChangePassword.as_view()), #change Password
path(r'contact_us/',Contact_US.as_view()), #Contact US
path(r'subscription/',Subscribe.as_view()), #Subscription API
path("UpdateProfile/<int:pk>/", UpdateProfile.as_view(), name="UpdateProfile"), #Update User Profile Details
path("UserProfile/<int:pk>", UserProfile.as_view(), name="UpdateProfile"), #View User Profile Details

]