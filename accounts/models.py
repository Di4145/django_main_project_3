from django.conf import settings
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar/%y/%m/%d/', blank=True)
    data = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.user}'

