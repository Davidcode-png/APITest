from rest_framework import serializers
from .models import  CommentReaction
from datetime import datetime

class CommentReactionSerializer(serializers.Serializer):
    comment_id = serializers.IntegerField()
    reaction = serializers.CharField(max_length=400)

    def create(self, validated_data):
        return CommentReaction(**validated_data)
