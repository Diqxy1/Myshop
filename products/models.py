from django.db import models
from categorys.models import Category

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    @property
    def abstract(self):
        return 'R${}'.format(self.price)
