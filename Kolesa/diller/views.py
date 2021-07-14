import logging

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models
from . import serializers

class One(APIView):
    def get(self):
        pass

logger = logging.getLogger(__name__)

@api_view(['GET', 'POST'])
def favorites_list(request):
    if request.method == 'GET':
        logger.debug('In get')

        favorites = models.Favourites.objects.all()
        serializer = serializers.FavouritesSerializer(favorites, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        logger.debug('In POST')

        serializer = serializers.FavouritesSerializer1(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
def favorites_detail(request, favourite_id):
    try:
        favorite = models.Favourites.objects.get(id=favourite_id)
    except models.Favourites.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = serializers.FavouritesSerializer(favorite)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = serializers.FavouritesSerializer1(instance=favorite, data=request.data)
        if serializer.is_valid():
            logger.info('DATA SAVED')

            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        favorite.delete()

        return Response({'deleted': True})

class ArchiveAPIView(APIView):
    def get(self, request):
        archive = models.Archive.objects.filter(user=self.request.user)
        #many=true
        serializer = serializers.ArchiveSerializer(archive, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.ArchiveSerializer1(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class PublicationsAPIView(APIView):
    def get(self, request):
        publication = models.Publications.objects.filter(user=self.request.user)
        serializer = serializers.PublicationSerializer(publication, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = serializers.PublicationSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class PublicationsDetailAPIView(APIView):
    def get(self,request, pub_id=None):
        publication = models.Publications.objects.get(id=pub_id)
        serializer = serializers.PublicationSerializer(publication, many=False)
        return Response(serializer.data)

