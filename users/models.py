from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from .utils import generate_ref_code


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    phone = models.CharField(max_length=11, blank=True)
    address = models.CharField(max_length=20, blank=True, null=True)

    male = 'male'
    female = 'female'
    
    gender_type = [
        ('male', male),
        ('female', female),
    ]

    gender= models.CharField(max_length=10, choices=gender_type, default=female)
    bio = models.TextField(max_length=150, blank=True)
    code = models.CharField(max_length=6, blank=True)    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    

#this function returns the profile name in the admin panel profile table
    def __str__ (self):
        return f'{self.user.username}-{self.code}'

    
    def save(self, *args, **kwargs):
        if self.code =="":
            code = generate_ref_code()
            self.code = code
        super().save(*args, **kwargs)


  


