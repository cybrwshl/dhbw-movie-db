from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from moviedb_backend.models import *


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('first_name', 'last_name', 'birthday')


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = ('name', 'budget', 'overview')


class KeywordSerializer(ModelSerializer):
    class Meta:
        model = Keyword
        fields = ('name', 'movie')


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = ('name',)


class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = ('file', 'title', 'description', 'attraction')

