from django.db import models


class Nations(models.Model):
    nation = models.CharField(max_length=100, verbose_name='Nations name')
    country = models.CharField(max_length=200, verbose_name='Country name')
    numb = models.IntegerField(verbose_name='Country number')
    flag = models.ImageField(upload_to='media', verbose_name='Country flag')

    def __str__(self):
        return self.nation

    class Meta:
        db_table = 'worldNation'
        verbose_name = 'Nations list'
