from .models import Bookmark
from django.contrib.auth.models import User, Group
from rest_framework import serializers

########## BookmarkSerializer
class BookmarkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bookmark
        fields = ['id', 'title', 'description', 'img']