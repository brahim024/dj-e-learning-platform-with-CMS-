from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Subject(models.Model):
	title=models.CharField(max_length=70)
	slug=models.SlugField(max_length=70,unique=True)
	class Meta:
		ordering=['title']
	def __str__(self):
		return self.title
class Course(models.Model):
	owner=models.ForeignKey(User,related_name='course_created',on_delete=models.CASCADE)
	subject=models.ForeignKey(Subject,related_name='courses',on_delete=models.CASCADE)
	title=models.CharField(max_length=70)
	slug=models.SlugField(max_length=70,unique=True)
	overview=models.TextField()
	created=models.DateTimeField(auto_now=True)
	class Meta:
		ordering=('-created')
	def __str__(self):
		return self.title