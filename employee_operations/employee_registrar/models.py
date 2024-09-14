from django.db import models
from PIL import Image
import os

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    photo = models.ImageField(upload_to='src/', default='src/default.jpg')

    def save(self, *args, **kwargs):
            super().save(*args, **kwargs)

            if self.photo:
                # Open the uploaded image
                img = Image.open(self.photo.path)

                # Resize the image to 250x250
                if img.height > 100 or img.width > 100:
                    output_size = (100, 100)
                    img = img.resize(output_size, Image.LANCZOS)
                    
                    # Save the resized image back to the same path
                    img.save(self.photo.path)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    