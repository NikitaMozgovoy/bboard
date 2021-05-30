from rest_framework import serializers
from .models import Bb, CustomUser, Rubric

class BbSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bb
        fields = '__all__'

class RubricSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rubric
        fields = '__all__'


class BbListRetrieveSerializer(serializers.ModelSerializer):
    rubric = RubricSerializer()

    class Meta:
        model = Bb
        fields = '__all__'

class UsersSerializer(serializers.modelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'