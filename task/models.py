from django.db import models


class Task(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=50)
    email=models.CharField(max_length=254)
    createdAt=models.DateTimeField(auto_now_add=True)

