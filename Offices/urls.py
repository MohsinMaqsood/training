from django.urls import path
from .views import *
urlpatterns = [
    path("state_list/", State.as_view(), name="state_list"),
    path("search_properties1/", Search_Properties1.as_view()),
    path("filter_properties1/", Filter_Properties1.as_view()),
    path("property_detail_by_id/<int:pk>/", Property_Detail_By_Id.as_view()),
    path("similar_properties/<int:pk>/", SimilarProperties.as_view()),
    path("state_properties/<state>/", State_Properties.as_view()),
    path("listing_services/", Listing_Services.as_view()),
    path("add_listing/", Add_Listing.as_view()),
    path("user_properties/", User_Properties.as_view()),
    path("get_put_del_property/<int:pk>", Get_Put_Del_Property.as_view()),
    path("user_favourite/<int:pk>", User_Favourite.as_view()),
    path("get_user_favourite/", Get_User_Favourite.as_view()),
    path("delete_user_favourite/<int:pk>", Delete_User_Favourite.as_view()),
    path("property_type/", PropertyType.as_view()),
    ################### For Testing ##################
    path("space_type/", SpaceType.as_view()),
]