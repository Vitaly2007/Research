from tabnanny import verbose
from django.db import models

class Subsidiary(models.Model):
    name = models.CharField(max_length=50, verbose_name='Name_subsidiary')

    class Meta:
        verbose_name_plural = 'Subsidiarys'
        verbose_name = 'Subsidiary'

    def __str__(self) -> str:
        return self.name

class Station(models.Model):
    title = models.CharField(max_length=50, verbose_name='Name_Station')
    subsidiary = models.ForeignKey(Subsidiary, on_delete=models.PROTECT, verbose_name='Subsidiary')

    class Meta:
        verbose_name = 'Station'

    def __str__(self) -> str:
        return self.title