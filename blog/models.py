from django.db import models
import datetime

class Blog(models.Model):
    title = models.CharField(max_length=255, default='')
    pub_date = models.DateField(default=datetime.date.today)
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%e %b %Y')

    def __str__(self):
        return self.title
