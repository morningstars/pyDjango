from django.contrib import admin

# Register your models here.

from . import models


class BookManager(admin.ModelAdmin):
    list_display = ['id', 'title','price', 'pub', 'pub_date']
    list_display_links = ['id', 'title']
    list_filter = ['pub']
    search_fields = ['pub']
    list_editable = ['price']


admin.site.register(models.Book, BookManager)
admin.site.register(models.Author)
admin.site.register(models.Wife)
