from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from account.serializers import *
from django.contrib.auth import authenticate
# Create your views here.

class UserRegistrationView(APIView):
    def post(self,request,formate=None):
        serializer=UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user=serializer.save()
            return Response({'msg':'Registration Success'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    def post(self,request,formate=None):
        serializer=UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email=serializer.data.get('email')
            password=serializer.data.get('password')

            user =authenticate(email=email,password=password)
            
            if user is not None:
                return Response({'msg':'Login Success'},status=status.HTTP_200_OK)
            else:
                return Response({'errors':{'non_field_errors':['Email or Password not valid']}},status=status.HTTP_404_NOT_FOUND)
        
        return Response(serializer.errors,status=status.HTTP_404_BAD_REQUEST)