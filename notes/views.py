from django.shortcuts import render
from .models import Notes
from rest_framework import generics, permissions

from random import randint

from django.contrib.auth.models import User

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import generics

from rest_framework import viewsets
from .serializers import Userserializer,NoteSerializer,QuoteSerializer

# Create your views here.

#notes manageent view
class NotesViewset(generics.ListCreateAPIView):
    serializer_class=NoteSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        return Notes.objects.filter(user=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(user=self.request.user)
        else:
            print(serializer.errors)


class QuotesViewset(generics.ListCreateAPIView):
    serializer_class = QuoteSerializer
    permission_classes = [AllowAny]  # Allow access to any user

    def get_queryset(self):
        count = Notes.objects.count()
        random_index = randint(0, count - 1)
        random_note = Notes.objects.all()[random_index]
        
        return [random_note]  # Return a single object in a list
   

#delte a file
            
class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Notes.objects.filter(user=user)


#usser creation view 
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = Userserializer
    permission_classes = [AllowAny]


#