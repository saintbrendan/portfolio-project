from django.db import models
import datetime

class Blog(models.Model):
    title = models.CharField(max_length=255, default='')
    pub_date = models.DateField(default=datetime.date.today)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')
