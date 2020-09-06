from rest_framework import serializers
from .models import Content


class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ('title', 'body', 'summary', 'doc_pdf', 'categories')
