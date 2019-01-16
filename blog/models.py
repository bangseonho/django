from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	text = models.TextField()
	create_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title

class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
	comment_user = models.ForeignKey(User, on_delete=models.CASCADE)
	comment_date = models.DateTimeField(auto_now_add=True)
	comment_content = models.CharField(max_length=100)

	def __str__(self):
		return self.comment_content
# Create your models here.
