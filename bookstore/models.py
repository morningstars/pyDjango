from django.db import models


# Create your models here.

class Author(models.Model):
    name = models.CharField('姓名', max_length=50, unique=True, db_index=True)
    age = models.IntegerField('年龄')
    email = models.EmailField('邮箱', null=True)

    def __str__(self):
        return "姓名：%s, 年龄：%d, 邮箱：%s" % (self.name, self.age, self.email)


class Book(models.Model):
    title = models.CharField('书名', max_length=50)
    price = models.DecimalField('定价', max_digits=7, decimal_places=2)
    pub = models.CharField('出版社名字', max_length=50, null=True)
    pub_date = models.DateField('出版时间', default='2020-01-01')

    # 增加多对一属性
    myAuthor = models.ForeignKey(Author, null=True)

    def __str__(self):
        return "id：%d, 书名：%s, 出版社：%s, 出版时间：%s" % (self.id, self.title, self.pub, self.pub_date)


class Wife(models.Model):
    name = models.CharField('姓名', max_length=50)
    age = models.IntegerField('年龄')
    # 增加一对一属性
    author = models.OneToOneField(Author)

    def __str__(self):
        return "姓名：%s， 年龄：%d" % (self.name, self.age)
