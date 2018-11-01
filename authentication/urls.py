from django.urls import path
from  authentication.views import UserList, UserDetail

urlpatterns = [
    path('users/', UserList.as_view()),
    path('user/<int:pk>', UserDetail.as_view()),
]