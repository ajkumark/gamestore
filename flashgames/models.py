from django.db import models

class Games(models.Model):
	name = models.CharField(max_length=50)
	description = models.TextField()
	filename = models.FileField(upload_to='/home/user/ajai/gamestore/uploads')
