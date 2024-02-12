from django.db import models


# Create your models here.
class Parent(models.Model):
    parent = models.CharField(max_length=200, unique=True)
    state = models.CharField(max_length=15, null=False, default='Active')
    
    def __str__(self):
        return self.parent


class Client(models.Model):
    parent_data = models.ForeignKey(Parent, on_delete=models.CASCADE, related_name='parent_info')
    client = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=15, null=False, default='Active')
    
    def __str__(self):
        return self.parent_data.parent
