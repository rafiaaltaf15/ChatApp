from rest_framework import serializers
from .models import Room
from .models import Message 

class RoomSerializer(serializers.ModelSerializer):   # also better to rename RooomSerializer → RoomSerializer
    class Meta:
        model = Room
        fields = "__all__"

class MessageSerializer(serializers.ModelSerializer):
    sender_username = serializers.CharField(source='sender.username',read_only=True)
    class Meta:
        model = Message
        fields = ['id', 'room', 'sender', 'sender_username', 'timestamp','text']