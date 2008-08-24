from django.db import models


class Calendar(models.Model):
	title = models.CharField(maxlength=200)
	year  = models.IntegerField()

	def __str__(self):
		return self.title


class Check(models.Model):
	day      = models.DateField()
	calendar = models.ForeignKey(Calendar)

	def __str__(self):
		return self.day
