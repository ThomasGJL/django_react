from django.db import models

# Create your models here.

class BookInfo(models.Model):
    id = models.BigAutoField(primary_key=True, null=False, help_text='主键')
    name = models.CharField(max_length=20, help_text='书名')
    author = models.CharField(max_length=20, help_text='作者')

    class Meta:
        db_table = 'book'
        verbose_name = '图书表'
