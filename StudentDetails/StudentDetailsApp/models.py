from django.db import models

# Create your models here.
class Student(models.Model): 
	name = models.CharField(max_length = 50) 
	section = models.CharField(max_length = 50)
	sno = models.CharField(max_length = 50) 
	phonenumber = models.IntegerField()
	class Meta:
	 	db_table = "Student" 

