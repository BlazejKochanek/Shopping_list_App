from django.db import models


class List(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)


class Product(models.Model):
    list = models.ForeignKey("List", on_delete=models.CASCADE)
    name = models.CharField()
    quantity = models.IntegerField
    is_bought = models.BinaryField(default=False)
