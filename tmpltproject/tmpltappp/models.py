from django.db import models

# Create your models here.
from django.db import models
# from .models import place
# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    image=models.ImageField(upload_to='pics')
    des=models.TextField()

    def __str__(self):
        return self.name
class member(models.Model):
        img=models.ImageField(upload_to='pic1')
        name=models.CharField(max_length=200)
        des1=models.TextField()

        def __str__(self):
            return self.name