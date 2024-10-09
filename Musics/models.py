from django.db import models
from django.contrib.auth.models import User

class Artists(models.Model):
    Username = models.OneToOneField(User,on_delete=models.CASCADE)
    Name = models.CharField(max_length=50,unique=True)
    
    def __str__(self) -> str:
        return f'{self.Name}'
class Musics(models.Model):
    Title = models.CharField(max_length=50)
    Singer = models.ForeignKey(Artists,on_delete=models.CASCADE)
    Cover = models.ImageField(upload_to='media/Covers')
    
    def __str__(self) -> str:
        return f'{self.Title} - {self.Singer}'
    