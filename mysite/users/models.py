from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class Collection(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name




class Link(models.Model):
    LINK_TYPES = (
        ('website', 'Website'),
        ('book', 'Book'),
        ('article', 'Article'),
        ('music', 'Music'),
        ('video', 'Video'),
    )
    collection = models.OneToOneField(Collection, on_delete=models.CASCADE, primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    image = models.URLField()
    link_type = models.CharField(max_length=20, choices=LINK_TYPES, default='website')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # Дополнительная логика, чтобы установить тип по умолчанию на 'website' и т.д.
        if not self.link_type:
            self.link_type = 'website'
        super().save(*args, **kwargs)


