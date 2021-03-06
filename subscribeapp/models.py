from projectapp.models import Project
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Subscription(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='subscription')
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='subscription')

    class Meta:
        unique_together = ('user', 'project')
