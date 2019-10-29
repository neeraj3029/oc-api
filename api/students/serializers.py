from rest_framework import serializers
from .models import User, Complaint

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'url', 'name', 'rollno')

class ComplaintSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Complaint
        fields = ('id', 'url', 'title', 'content', 'cuser', 'status')