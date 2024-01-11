from django.db import models


# Create your models here.
class Parent(models.Model):
    parent = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.parent


class Client(models.Model):

    parent_data = models.ForeignKey(Parent, on_delete=models.CASCADE)
    # parent = models.ManyToManyField(Parent)
    parent_company = models.CharField(max_length=200, default='')
    client = models.CharField(max_length=200)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.client