from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length = 50)
    email=models.EmailField()
    phone=models.IntegerField()
    subscribe=models.CharField(max_length = 50)
    gender=models.CharField(max_length = 50)
    dob=models.DateField()
    profile_pic=models.ImageField(upload_to = 'image/')
    password=models.CharField(max_length = 50)
    
    def __str__(self):
        return self.name