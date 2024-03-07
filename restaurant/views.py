from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from .serializers import MenuSerializer, BookingSerializer, UserSerializer
from .models import Menu, Booking
from django.contrib.auth.models import User

# Create your views here.
def index(request):
  return render(request, 'index.html', {})

class MenuItemsView(generics.ListCreateAPIView):
  queryset = Menu.objects.all()
  serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
  queryset = Menu.objects.all()
  serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
  queryset = Booking.objects.all()
  serializer_class = BookingSerializer
  permission_classes = [IsAuthenticated]

class UserViewSet():
  queryset = User.objects.all()
  serializer_class = UserSerializer
