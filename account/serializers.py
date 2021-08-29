from rest_framework import serializers
from account.models import Account


class RegistrationSerializer(serializers.ModelSerializer):

    repeat_password = serializers.CharField(style={'input_type': 'password'})

    class Meta:
        model = Account
        fields = ["email", 'username', 'password', 'repeat_password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        account = Account(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password = self.validated_data['password']
        repeat_password = self.validated_data['repeat_password']

        if password != repeat_password:
            raise serializers.ValidationError({'password': 'Passwords must watch'})
        account.set_password(password)
        account.save()
        return account
