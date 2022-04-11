from django.db import models

# Create your models here.
class Contact_us(models.Model):
    Name= models.CharField(max_length=32)
    Email= models.EmailField()
    Subject= models.CharField(max_length=40)
    Message= models.TextField()
