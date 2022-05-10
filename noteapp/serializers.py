from rest_framework import serializers
from .models import Notes

class NotesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Notes
        fields = ['id', 'name_id', 'name', 'subject']