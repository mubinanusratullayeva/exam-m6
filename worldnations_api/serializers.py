from rest_framework import serializers

from worldnation.models import Nations


class NationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nations
        fields = ('nation', 'country', 'numb', 'flag', )
