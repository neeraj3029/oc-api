from rest_framework import serializers
from .models import User

class UserSearializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'name', 'rollno')