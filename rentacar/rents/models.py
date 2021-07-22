from django.db import models

from clients.models import Client
from companys.models import Company

# Create your models here.

class Rent(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='client_rents')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_rents')
    daily_cost = models.IntegerField()
    days = models.IntegerField()

    class Meta:
        ordering = ('company',)
        verbose_name = 'Arriendo'
        verbose_name_plural = 'Arriendos'

    def __str__(self):
        return self.company.name
