from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status, permissions
from missional_community.serializers import MissionalCommunitySerializer
from missional_community.models import MissionalCommunity


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def missional_community_list(request):
    """
    List all MCs or add a new one
    """
    if request.method == "GET":
        missional_communities = MissionalCommunity.objects.all()
        serializer = MissionalCommunitySerializer(missional_communities, many=True)
        return Response(serializer.data)
   
    elif request.method == "POST":
        serializer = MissionalCommunitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST','DELETE'])
@permission_classes((permissions.AllowAny,))
def missional_community_detail(request, id):
    """
    Retrieve, update or delete an MC
    """
    try:
        missional_community = MissionalCommunity.objects.get(pk=id)
    except MissionalCommunity.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = MissionalCommunitySerializer(missional_community)
        return Response(serializer.data)
   
    elif request.method == "PUT":
        serializer = MissionalCommunitySerializer(missional_community, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    elif request.method == "DELETE":
        missional_community.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)