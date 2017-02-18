from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Kyoten(models.Model):
    area = models.CharField(max_length=200)

    def __str__(self):
        return self.area

class Nori(models.Model):
    user = models.ForeignKey(User)
    date = models.DateTimeField('departure date')
    departure = models.ForeignKey(Kyoten, related_name='+')
    arrival = models.ForeignKey(Kyoten, related_name='+')
    comment = models.CharField(max_length=200)

    def __str__(self):
        return self.comment

class Comment(models.Model):
    nori = models.ForeignKey(Nori, related_name='+')
    user = models.ForeignKey(User)
    comment = models.CharField(max_length=200)

    def __str__(self):
        return self.comment
