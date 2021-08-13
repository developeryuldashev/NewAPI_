from django.db import models


class Article(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField()
    tags = models.CharField(max_length=300)
    published_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
class LinkedFiles(models.Model):
    article=models.ForeignKey(Article, on_delete=models.CASCADE)
    file=models.FileField()
    describtion=models.CharField(max_length=200)
    @property
    def fileURL(self):
        try:
            return self.file.url
        except:
            return ''

### bu yerda tariflar modeli bor
class Tarifs(models.Model):
    tarif_name=models.CharField(max_length=200)
    price=models.IntegerField()
    discribtion=models.CharField(max_length=300)
    possiblity=models.CharField(max_length=300)

    def __str__(self):
        return self.tarif_name
class Services(models.Model):
    servic_name=models.CharField(max_length=250)
    iconca=models.ImageField(null=True)
    body=models.TextField()
    @property
    def iconURL(self):
        try:
            return self.iconca.url
        except:
            return ''

class Experts(models.Model):
    full_name=models.CharField(max_length=200)
    job=models.CharField(max_length=200, null=True)
    level = models.CharField(max_length=100, null=True)
    image=models.ImageField(null=True)
    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''
class Results(models.Model):
    name=models.CharField(max_length=300)
    body=models.TextField()
    image = models.ImageField(null=True)
    @property
    def imageURL(self):
        try:
            return self.image.url
        except:
            return ''

    






