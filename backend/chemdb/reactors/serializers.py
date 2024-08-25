from rest_framework import serializers
from .models import Reactor

class ReactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reactor
        fields = '__all__'
