from django.db import models


# Create your models here.
class Supplier(models.Model):
    first_name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    dni = models.IntegerField()

    def __str__(self):
        return f'{self.first_name} {self.surname} - {self.dni}'


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    current_stock = models.IntegerField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}: ${self.price}'
