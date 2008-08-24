from django.db import models


class Calendar(models.Model):
	title = models.CharField(maxlength=200)
	year  = models.IntegerField()

	def __str__(self):
		return self.title

	class Admin:
		pass


class Check(models.Model):
	day      = models.DateField(core=True)
	calendar = models.ForeignKey(Calendar, edit_inline=models.TABULAR, num_in_admin=5, num_extra_on_change=5)

	def __str__(self):
		return self.day.strftime("%d/%m/%Y")
