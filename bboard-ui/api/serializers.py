from rest_framework import serializers

from bboard.models import Bb, Rubric, CustomUser

class BbSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bb
        fields='__all__'


class BbRubricSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rubric
        fields='__all__'

class BbListRetrieveSerializer(serializers.ModelSerializer):
    rubric = BbRubricSerializer()

    class Meta:
        model = Bb
        fields = '__all__'

