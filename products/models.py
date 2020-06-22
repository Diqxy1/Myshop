from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=40)
    category = models.CharField(max_length=40)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title

    @property
    def abstract(self):
        return 'R${}'.format(self.price)


class Category(models.Model):
    title = models.CharField(max_length=40)

    def __str__(self):
        return self.title
