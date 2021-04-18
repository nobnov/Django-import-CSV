from django.db import models


# Create your models here.
class Guest(models.Model):
    name = models.CharField(max_length=20)
    job = models.CharField(max_length=10)
    age = models.IntegerField()

    class Meta:
        db_table = 'guest'
        verbose_name = 'ゲスト'
        verbose_name_plural = 'ゲスト一覧'

    def __str__(self):
        return self.name
