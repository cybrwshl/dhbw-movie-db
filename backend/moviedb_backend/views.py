from django.shortcuts import render
from rest_framework import viewsets
from moviedb_backend.serializers import *

# Create your views here.


class PersonViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class KeywordViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Keyword.objects.all()
    serializer_class = KeywordSerializer


class CompanyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class RoleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


#class PersonViewSet(viewsets.ModelViewSet):
#    queryset = Person.objects.all()
#    serializer_class = PersonSerializer
#
#
#class MovieViewSet(viewsets.ModelViewSet):
#    queryset = Movie.objects.all()
#    serializer_class = MovieSerializer
#
#
#class KeywordViewSet(viewsets.ModelViewSet):
#    queryset = Keyword.objects.all()
#    serializer_class = KeywordSerializer
#
#
#class CompanyViewSet(viewsets.ModelViewSet):
#    queryset = Company.objects.all()
#    serializer_class = CompanySerializer
#
#
#class RoleViewSet(viewsets.ModelViewSet):
#    queryset = Role.objects.all()
#    serializer_class = RoleSerializer
