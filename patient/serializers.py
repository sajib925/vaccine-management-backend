from rest_framework import serializers
from django.contrib.auth.models import User
from . import models
from django.utils.translation import gettext_lazy as _

class PatientSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = models.Patient
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("Passwords do not match")
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError("Email already exists")
        return data

    def create(self, validated_data):
        validated_data.pop('confirm_password')
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            is_active=True
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


# class UserLoginSerializer(serializers.Serializer):
#     username = serializers.CharField(required=True)
#     password = serializers.CharField(required=True, write_only=True)
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    def validate_username(self, value):
        if not User.objects.filter(username=value).exists():
            raise serializers.ValidationError(_("The username you entered does not exist."))
        return value

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError(_("Password must be at least 8 characters long."))
        return value

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        user = User.objects.filter(username=username).first()

        if user and not user.check_password(password):
            raise serializers.ValidationError({"password": _("Invalid password. Please try again.")})

        if user is None:
            raise serializers.ValidationError({"username": _("The username you entered does not exist.")})

        return data


class ProfileUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']

    def update(self, instance, validated_data):
        if 'username' in validated_data:
            raise serializers.ValidationError({"username": "Username cannot be updated."})
        return super().update(instance, validated_data)


class PasswordUpdateSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True, write_only=True)
    new_password = serializers.CharField(required=True, write_only=True)
    confirm_password = serializers.CharField(required=True, write_only=True)

    def validate(self, data):
        user = self.context['request'].user
        if not user.check_password(data['old_password']):
            raise serializers.ValidationError({"old_password": "Old password is incorrect."})
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError({"confirm_password": "New passwords do not match."})
        return data

    def update(self, instance, validated_data):
        instance.set_password(validated_data['new_password'])
        instance.save()
        return instance































# from rest_framework import serializers
# from . import models
# from django.contrib.auth.models import User




# class PatientSerializer(serializers.ModelSerializer):
#     user = serializers.StringRelatedField(many=False)
#     class Meta:
#         model = models.Patient
#         fields = '__all__'




# class RegistrationSerializer(serializers.ModelSerializer):
#     confirm_password = serializers.CharField(required=True, write_only=True)

#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']
    
#     def save(self, **kwargs):
#         username = self.validated_data['username']
#         first_name = self.validated_data['first_name']
#         last_name = self.validated_data['last_name']
#         email = self.validated_data['email']
#         password = self.validated_data['password']
#         confirm_password = self.validated_data['confirm_password']
        
#         if password != confirm_password:
#             raise serializers.ValidationError({'error': "Passwords do not match"})
#         if User.objects.filter(email=email).exists():
#             raise serializers.ValidationError({'error': "Email already exists"})
        
#         # Create and save the user
#         user = User(
#             username=username,
#             email=email,
#             first_name=first_name,
#             last_name=last_name,
#             is_active=True  # Activate the user immediately
#         )
#         user.set_password(password)
#         user.save()
        
#         return user



# class UserLoginSerializer(serializers.Serializer):
#     username = serializers.CharField(required = True)
#     password = serializers.CharField(required = True)


# # class RegistrationSerializer(serializers.ModelSerializer):
# #     confirm_password = serializers.CharField(required = True)
# #     class Meta:
# #         model = User
# #         fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']
    
# #     def save(self):
# #         username = self.validated_data['username']
# #         first_name = self.validated_data['first_name']
# #         last_name = self.validated_data['last_name']
# #         email = self.validated_data['email']
# #         password = self.validated_data['password']
# #         password2 = self.validated_data['confirm_password']
        
# #         if password != password2:
# #             raise serializers.ValidationError({'error' : "Password Doesn't Mactched"})
# #         if User.objects.filter(email=email).exists():
# #             raise serializers.ValidationError({'error' : "Email Already exists"})
# #         account = User(username = username, email=email, first_name = first_name, last_name = last_name)
# #         print(account)
# #         account.set_password(password)
# #         account.is_active = False
# #         account.save()
# #         return account