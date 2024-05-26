from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class StoreModel(models.Model):
    profile_pic = models.ImageField(blank=True, null=True)
    user = models.ForeignKey(User, max_length=10, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return f'profile pic of {self.user}'


