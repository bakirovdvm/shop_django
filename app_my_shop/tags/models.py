from django.db import models
from rest_framework.views import APIView

from product.models import Tag


# class TagsView(APIView):
#     def get(self, request):
#         tags = Tag.objects.all()
#         print(tags)
