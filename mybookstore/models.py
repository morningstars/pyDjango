from django.db import models


# Create your models here.

class MyAuthor(models.Model):
    name = models.CharField('姓名', max_length=50)

    def __str__(self):
        return "姓名：" + self.name


class MyBook(models.Model):
    title = models.CharField('书名', max_length=50)

     # 一对多
    author = models.ForeignKey(MyAuthor, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "书名：" + self.title
