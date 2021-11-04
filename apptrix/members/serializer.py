from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from django.contrib.auth import get_user_model, authenticate

from members.models import Member


class MemberSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = Member
        fields = ('email', 'password', 'first_name', 'last_name', 'gender', 'photo', 'token')

    def create(self, validated_data):
        return Member.objects.create_user(**validated_data)
