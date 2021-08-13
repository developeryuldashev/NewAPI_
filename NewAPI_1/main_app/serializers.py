from rest_framework import serializers
from .models import *

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Article
        fields='__all__'

class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model=LinkedFiles
        fields='__all__'

class TarifsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tarifs
        fields="__all__"

class ServicSerializer(serializers.ModelSerializer):
    class Meta:
        model=Services
        fields='__all__'

class ExpertSerializer(serializers.ModelSerializer):
    class Meta:
        model=Experts
        fields='__all__'

class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model=Results
        fields='__all__'