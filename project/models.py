from django.db import models

from cloudinary.models import CloudinaryField

# Create your models here.

class Project(models.Model):
    project_name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(unique=True, null=False)
    description = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    alt_image = models.CharField(max_length=300, null=False)
    client_name = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    finished = models.BooleanField(default=False)
    tagline = models.CharField(max_length=50)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.project_name