from django.contrib import admin

# Register your models here.

from . import models
admin.site.register(models.MyAuthor)
admin.site.register(models.MyBook)
