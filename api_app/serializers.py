from rest_framework import serializers
from .models import Ceos


class CeosSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ceos
        fields = ['name', 'year_started']
