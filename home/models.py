from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class HomeHeaderModel(models.Model):
    slogan = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.slogan


class HomeCommentModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    rate = models.IntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ])

    def __str__(self):
        return f'{self.user.username} - {self.body}'


class Badge(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Insights(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='insights/images/')
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

