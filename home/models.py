from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.text import slugify


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


class InsightModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='insights/images/')
    badge = models.ForeignKey(Badge, on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True, unique=True)

    def __str__(self):
        return self.title

    def save(
            self,
            *args, **kwargs
    ):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class SocialModel(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class ApplicationLinksModel(models.Model):
    name = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class FreedomBackModel(models.Model):
    image = models.ImageField(upload_to='freedom/images/')
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
