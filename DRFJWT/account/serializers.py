from rest_framework import serializers
from account.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
  # We are writing this becoz we need confirm password field in our Registratin Request
  password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
  class Meta:
    model = User
    fields=['email', 'name', 'password', 'password2', 'tc']
    extra_kwargs={
      'password':{'write_only':True}
    }

  # Validating Password and Confirm Password while Registration
  def validate(self, attrs):
    password = attrs.get('password')
    password2 = attrs.get('password2')
    if password != password2:
      raise serializers.ValidationError("Password and Confirm Password doesn't match")
    return attrs

  def create(self, validate_data):
    return User.objects.create_user(**validate_data)


class UserLoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=255)
    class Meta:
        model= User
        fields=['email','password']


class UserProfileSerializer(serializers.ModelSerializer):
  
  class Meta:
    model=User
    fields=['id','email','name']


class UserChangePasswordSerializer(serializers.Serializer):
  password = serializers.CharField(style={'input_type':'password'}, write_only=True)
  password2 = serializers.CharField(style={'input_type':'password'}, write_only=True)
  
  class Meta:
    fields=['password','password2']

  
  def validate()

