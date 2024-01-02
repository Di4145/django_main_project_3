from django.db import models
from django.urls import reverse


# Create your models here.


class Type(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Maker(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=30)
    maker = models.ForeignKey(Maker, on_delete=models.CASCADE)
    LEFT_STATUS = [('min', 'Осталось мало'), ('max', 'Осталось много'), ('mid', 'Осталось достаточно')]
    left = models.CharField(max_length=10, choices=LEFT_STATUS, default='min')
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    info = models.TextField()
    cover = models.ImageField(upload_to='product_cover', blank=True)
    on_site = models.BooleanField(default=False)
    sale = models.FloatField()
    cost = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail_shop', args=[str(self.id)])
