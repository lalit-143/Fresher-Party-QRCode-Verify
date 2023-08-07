from django.db import models

# Create your models here.

class Student(models.Model):
	
	name = models.CharField(max_length = 100)
	number = models.CharField(max_length = 100)
	attemps = models.IntegerField(default = 0)

	def __str__(self):
		return self.name + " --- " + self.number + " ---> " + str(self.attemps)

	