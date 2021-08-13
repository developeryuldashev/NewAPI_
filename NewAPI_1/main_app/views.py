from django.shortcuts import render
from rest_framework.response import Response
from .serializers import *
from rest_framework import viewsets


class ArticleView(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
class ArticleByTagView(viewsets.ModelViewSet):
    queryset=Article.objects.all()
    serializer_class = ArticleSerializer
    def retrieve(self, request, *args, **kwargs):
        tag=kwargs['pk']
        print(tag)
        articles=self.queryset.filter(tags__contains=tag)
        print(articles)
        data =[]
        for article in articles:
            d={
                'id':article.id,
                'title':article.name,
                'body':article.text,
                'tags':article.tags,
            }
            data.append(d)
        return Response({'data':data})

class FileView(viewsets.ModelViewSet):
    queryset = LinkedFiles.objects.all()
    serializer_class = FileSerializer

class TarifView(viewsets.ModelViewSet):
    queryset =Tarifs
    serializer_class = TarifsSerializer

class ServicView(viewsets.ModelViewSet):
    queryset = Services
    serializer_class = ServicSerializer

class ExpertView(viewsets.ModelViewSet):
    queryset = Experts
    serializer_class = ExpertSerializer

class ExpertByLevelView(viewsets.ModelViewSet):
    queryset = Experts.objects.all()
    serializer_class = ExpertSerializer
    def retrieve(self, request, *args, **kwargs):
        level=kwargs['pk']
        experts=self.queryset.filter(level__contains=level)
        data=[]
        for expert in experts:
            d={
                'id':expert.id,
                'full_name':expert.full_name,
                'level':expert.level,
                'job':expert.job,
                'image':expert.imageURL()
            }
            data.append(d)
        return Response({'data':data})

class ResultView(viewsets.ModelViewSet):
    queryset = ResultSerializer
    serializer_class = ResultSerializer


