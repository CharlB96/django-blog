from django.db import models

# Create your models here.

class About(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:

        def __str__(self):
            return f"{self.title}"