from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from product.models import Tag
from .serializers import TagSerializer


class TagsView(APIView):
    '''
    Описывается работа облака тэгов, то есть при нажатии мышкой на какойнибудь тэг,
    передается Id и Имя тэга
    '''

    def get(self, request):
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)


        return Response(serializer.data)
