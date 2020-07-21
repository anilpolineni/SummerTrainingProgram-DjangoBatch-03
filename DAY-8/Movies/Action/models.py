from django.db import models

# Create your models here.
class Studentform(models.Model):
	s_name=models.CharField(max_length=50)
	s_age=models.IntegerField()
	s_roll=models.CharField(max_length=10)
	s_email=models.EmailField(max_length=100)

	def __str__(self):
		return self.s_name+' '+self.s_roll

class Actors(models.Model):
	a_name=models.CharField(max_length=100)
	a_age=models.IntegerField()
	a_no_movies=models.IntegerField()

	def __str__(self):
		return self.a_name+str(self.a_age)