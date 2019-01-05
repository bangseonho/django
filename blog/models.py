from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	text = models.TextField()
	create_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title


# Create your models here.
