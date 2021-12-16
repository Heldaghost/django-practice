from django.contrib.auth.models import User
from rest_framework import serializers
from phone_book.models import *


class PhoneNoteSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = PhoneNote
        fields = ('url', 'id', 'first_name', 'last_name', 'phone_number', 'is_friend', 'created_at', 'user')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    notes = serializers.HyperlinkedRelatedField(many=True, view_name='phonenote-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'notes']
