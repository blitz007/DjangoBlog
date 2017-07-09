from django.db import models
from django.utils import timezone
class Post(models.Model):
	topic=models.CharField(max_length=100)
	content=models.TextField()
	pub_date=models.DateTimeField('published_date')
	votes=models.IntegerField(default=0)

	def __str__(self):
		return self.topic

class Comment(models.Model):
	post = models.ForeignKey(Post,on_delete=models.CASCADE)
	pub_date=models.DateTimeField('comment_date')
	text=models.CharField(max_length=400)

	

# Create your models here.
