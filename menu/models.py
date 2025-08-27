from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    featured_image = CloudinaryField('image', blank=True, null=True, default='https://res.cloudinary.com/dmzw6gxps/image/upload/v1753708918/s2s5ltkbp0lr5gt9pote.jpg')
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.name
