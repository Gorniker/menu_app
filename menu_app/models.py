from django.db import models

# Create your models here.
class Topping(models.Model):
    class Meta:
        db_table = 'Topping'

    name = models.TextField()


class FoodCategory(models.Model):
    class Meta:
        db_table = 'FoodCategory'

    name = models.TextField()
    is_publish = models.BooleanField()

class Food(models.Model):
    class Meta:
        db_table = 'Food'

    category = models.ForeignKey(FoodCategory, on_delete=models.PROTECT)
    description = models.TextField()
    price = models.IntegerField()
    is_special = models.BooleanField()
    is_vegan = models.BooleanField()
    is_publish = models.BooleanField()
    toppings = models.ManyToManyField(Topping,db_column='toppings')
