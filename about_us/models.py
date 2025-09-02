from django.db import models

# Create your models here.
class AboutUs(models.Model):
    """Model to store About Us page information."""

    title = models.CharField(max_length=100)
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    #changes the name to readabe text in admin panel