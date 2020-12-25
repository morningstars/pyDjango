from django.db import models


# Create your models here.

class Book(models.Model):
    title = models.CharField('书名', max_length=50)
    price = models.DecimalField('定价', max_digits=7, decimal_places=2)
    pub = models.CharField('出版社名字', max_length=50, null=True)
    pub_date = models.DateField('出版时间', default='2020-01-01', null=False)


class Author(models.Model):
    name = models.CharField('姓名', max_length=50, null=False, unique=True, db_index=True)
    age = models.IntegerField('年龄', null=False)
    email = models.EmailField('邮箱', null=True)
