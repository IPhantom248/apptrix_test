from rest_framework import serializers

from members.models import Member


class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Member
        fields = ('email', 'password', 'first_name', 'last_name', 'gender', 'photo')
        write_only_fields = ['password']

    def create(self, validated_data):
        return Member.objects.create_user(**validated_data)


class MemberListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('first_name', 'last_name', 'gender', 'photo')



