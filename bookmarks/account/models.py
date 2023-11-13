from django.contrib.auth.models import User
from django.db import models
from django.db.models import CASCADE


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=CASCADE)
    date_of_birth = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',blank=True)

    def __str__(self):
        return f" profile of {self.user.username}"
