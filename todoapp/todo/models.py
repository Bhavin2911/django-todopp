from django.db import models

# Create your models here.
class todoitem(models.Model):
	content=models.TextField()
