from django.shortcuts import render
from rest_framework import viewsets, generics
from .models import User, Complaint
from .serializers import UserSerializer, ComplaintSerializer

# Create your views here.
class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ComplaintView(viewsets.ModelViewSet):
    queryset = Complaint.objects.all()
    serializer_class = ComplaintSerializer


    
    

