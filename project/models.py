from django.db import models

from cloudinary.models import CloudinaryField

# Create your models here.
STATUS = ((0, "Draft"), (1, "Pending Approval"), (2, "Published"))

class Project(models.Model):
    project_name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(unique=True, null=False)
    description = models.TextField()
    featured_image = CloudinaryField('image', default='placeholder')
    client_name = models.CharField(max_length=30)
    location = models.CharField(max_length=50)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    finished = models.BooleanField(default=False)
    tagline = models.CharField(max_length=50)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.project_name