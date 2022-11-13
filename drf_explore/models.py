from django.db import models

# Create your models here.


class Project(models.Model):

	project_name = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)

	