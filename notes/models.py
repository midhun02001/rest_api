from django.db import models
from django.contrib.auth.models import User



class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(default='')
    author = models.CharField(max_length=100,default='')
    create = models.DateField(auto_now_add=True)

    
