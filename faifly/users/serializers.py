from rest_framework import serializers

from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

from api.models.worker import Worker
from users.models import Roles

User = get_user_model()




class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    default_error_messages = {
        "no_active_account": ("Incorrect login or password")
    }
    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data['refresh'] = str(refresh)
        # data.pop('refresh', None) # remove refresh from the payload
        data['access'] = str(refresh.access_token)

        # Add extra responses here
        data['username'] = self.user.username
        data['email'] = self.user.email
        data['role'] = self.user.role
        data['id'] = self.user.pk
        if self.user.role == Roles.WORKER:
            data['worker_id'] = self.user.worker.pk
        return data

class RegisterSerializer(serializers.ModelSerializer):


    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2', 'email','role')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs



    def create(self, validated_data):
        if validated_data['role'] == Roles.WORKER:
            user = User.objects.create(
                username=validated_data['username'],
                email=validated_data['email'],
                role=validated_data['role'],
                worker=Worker.objects.create(
                    full_name=validated_data['email'],
                ),




            )
        else:
            user = User.objects.create(
                username=validated_data['username'],
                email=validated_data['email'],
                role=validated_data['role'],
                )


        user.set_password(validated_data['password'])
        user.save()
        # refresh = self.get_token(user)
        # user['refresh'] = str(refresh)
        # # data.pop('refresh', None) # remove refresh from the payload
        # user['access'] = str(refresh.access_token)
        return user


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    default_error_message = {
        'bad_token': ('Token is expired or invalid')
    }

    def validate(self, attrs):
        self.token = attrs['refresh']
        return attrs

    def save(self, **kwargs):

        try:
            RefreshToken(self.token).blacklist()

        except TokenError:
            self.fail('bad_token')