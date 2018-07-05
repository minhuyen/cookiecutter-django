from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_auth.serializers import TokenSerializer
from drf_base64.fields import Base64ImageField
# get the UserModel
UserModel = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):
    """
    User model w/o password
    """

    avatar = Base64ImageField(required=False)

    class Meta:
        model = UserModel
        fields = ('pk', 'username', 'email', 'avatar', 'first_name',
                  'last_name', 'referral_code', 'referrer',
                  'bommers', 'lives', 'best_score')
        read_only_fields = ('email', )


class CustomTokenSerializer(TokenSerializer):
    user = UserDetailSerializer(read_only=True)

    class Meta(TokenSerializer.Meta):
        fields = TokenSerializer.Meta.fields + ('user', )
