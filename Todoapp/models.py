from django.db import models
from datetime import datetime

# Create your models here.
class List(models.Model):
	list_item = models.CharField(max_length=200)
	created_at = models.DateTimeField(default=datetime.now,blank=True)
 	