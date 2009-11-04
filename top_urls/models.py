from django.db import models


class top_url(models.Model):
    url = models.CharField(max_length=200)
    rank = models.IntegerField()
    date_added = models.DateTimeField('date added')
   
