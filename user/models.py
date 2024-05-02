from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    fullname= models.CharField(max_length=100,default='hello world')
    image = models.ImageField(upload_to='profile_pictures',default='default_avatar.png')
    location = models.CharField(max_length=100,blank=True)
    age = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(100)],default=10)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default='O')
    def __str__(self):
        return self.fullname
    
