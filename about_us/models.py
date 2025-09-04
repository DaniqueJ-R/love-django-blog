from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class AboutUs(models.Model):
    """Model to store About Us page information."""

    title = models.CharField(max_length=100)
    profile_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    #changes the name to readabe text in admin panel

class CollaborateRequest(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"