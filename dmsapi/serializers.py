from django.db.models import fields
from rest_framework import serializers
from .models import Document, Typification


class TypificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Typification
        fields = ('id', 'name',)


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('id', 'name', 'type_document', 'amount', 'typification', 'price', 'image','created_at', 'updated_at',)

