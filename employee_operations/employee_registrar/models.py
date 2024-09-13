from django.db import models

# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    #photo = models.ImageField(upload_to='employee_photos/')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    