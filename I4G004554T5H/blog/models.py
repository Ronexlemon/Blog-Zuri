from wsgiref.handlers import format_date_time
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Post(models.Model):
    Title= models.CharField(max_length=200)
    Text = models.TextField(max_length=40000,null=False,editable=True)
    Author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    Created_date = models.DateTimeField(auto_now=True)
    Published_date = models.DateField(auto_now=True)

    def __str__(self):
       return( self.Title,self.Author,self.Text,self.Created_date,self.Published_date)


