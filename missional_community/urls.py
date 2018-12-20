from django.urls import path
from missional_community.views import missional_community_list, missional_community_detail

urlpatterns = [
    path('', missional_community_list),
    path('<int:id>', missional_community_detail),
]