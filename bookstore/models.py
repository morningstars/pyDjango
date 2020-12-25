from django.db import models


# Create your models here.

class Book(models.Model):
    title = models.CharField('书名', max_length=50)
    price = models.DecimalField('定价', max_digits=7, decimal_places=2)
    pub = models.CharField('出版社名字', max_length=50, null=True)