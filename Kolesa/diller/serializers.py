from rest_framework import serializers

from auth_.serializers import UserSerializer
from diller import models

class PublicationSerializer(serializers.ModelSerializer):
    user = UserSerializer(source='user.profile', read_only=True)

    class Meta:
        model = models.Publications
        fields = 'city', 'title', 'description', 'price', 'year', 'user', 'image'
    def create(self, validated_data):
        favorite = models.Publications.objects.create(user=self.context['request'].user,
                                                    city=validated_data.get('city'),
                                                      title=validated_data.get('title'),
                                                      description=validated_data.get('description'),
                                                      price=validated_data.get('price'),
                                                      year=validated_data.get('year'),
                                                      image=validated_data.get('image'))
        return favorite

class FavouritesSerializer(serializers.ModelSerializer):
    user = UserSerializer(source='user.profile', read_only=True)
    publications = PublicationSerializer(read_only=True)

    class Meta:
        model = models.Favourites
        fields = '__all__'


class ArchiveSerializer(serializers.ModelSerializer):
    #user pulications
    user = UserSerializer(source='user.profile', read_only=True)
    publications = PublicationSerializer(read_only=True)

    class Meta:
        model = models.Archive
        fields = '__all__'


class FavouritesSerializer1(serializers.Serializer):
    user = serializers.IntegerField(write_only=True)
    publications = serializers.IntegerField(write_only=True)

    def create(self, validated_data):
        favorite = models.Favourites.objects.create(user_id=validated_data.get('user'),
                                                    publications_id=validated_data.get('publications'))
        return favorite

class ArchiveSerializer1(serializers.Serializer):
    user = serializers.IntegerField(write_only=True)
    publications = serializers.IntegerField(write_only=True)

    def create(self, validated_data):
        archive = models.Archive.objects.create(user_id=validated_data.get('user'),
                                                    publications_id=validated_data.get('publications'))
        return archive
