from rest_framework import serializers
from phone_book.models import *


class PhoneNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNote
        fields = ('id', 'first_name', 'last_name', 'is_friend', 'created_at')