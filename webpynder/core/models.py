from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50, null=True)
    age = models.IntegerField(null=True)
    bio = models.TextField(null=True)
    profile_photo = models.TextField(null=True)
    photo_list = models.TextField(null=True)
    user_id = models.CharField(null=True, max_length=100)