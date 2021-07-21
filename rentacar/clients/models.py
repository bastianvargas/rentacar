from django.db import models

# Create your models here.

class Client(models.Model):
    rut = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.name
