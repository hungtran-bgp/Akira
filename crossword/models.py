from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Crossmap(models.Model):
    title = models.CharField(max_length = 20)
    grid_size = models.PositiveIntegerField(default=15)
    level = models.PositiveSmallIntegerField(default = 0)
    picture = models.ImageField(upload_to='crossword_pictures',default='crossword_default.png')
    def __str__(self):
        return self.title

class Word(models.Model):
    crossmap = models.ForeignKey(Crossmap,on_delete = models.CASCADE)
    text = models.CharField(max_length = 20)
    row = models.PositiveSmallIntegerField()
    clue = models.CharField(blank = True, max_length=500)

    def __str__(self):
        return self.clue
class CrossmapResult(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    crossmap = models.ForeignKey(Crossmap,on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    def __str__(self):
        return f"user:{self.user.username} - crossmap:{self.crossmap.title} - score{self.score}" 
class WordResult(models.Model):
    crossmap_result= models.ForeignKey(CrossmapResult,on_delete=models.CASCADE)
    text = models.CharField(max_length=20)
    row = models.IntegerField(default=1)
    wordCheck = models.BooleanField(default=0)

   