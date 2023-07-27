from django.db import models

# Create your models here.
class Movies(models.Model):
    objects = None
    name=models.CharField(max_length=250)
    des=models.TextField()
    year=models.IntegerField()
    img=models.ImageField(upload_to='pic')


    def __str__(self):
        return  self.name