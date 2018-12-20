from rest_framework.serializers import ModelSerializer
from missional_community.models import MissionalCommunity

class MissionalCommunitySerializer(ModelSerializer):
    class Meta:
        model = MissionalCommunity
        fields = ('name', 'location', 'leader', 'assistant', 
                    'church_location', 'frontier')
