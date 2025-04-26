from django.db import models
from django.contrib.auth.models import User



class Task(models.Model):
    TODO = 'To Do'
    IN_PROGRESS = 'In Progress'
    COMPLETED = 'Completed'

    STATUS_CHOICE = (
        (TODO, TODO),
        (IN_PROGRESS, IN_PROGRESS),
        (COMPLETED, COMPLETED)
    )

    title = models.CharField(max_length=255)
    details = models.TextField(null=True)
    status = models.CharField(max_length=255, choices=STATUS_CHOICE,default=TODO)
    deadline = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.owner.username}: {self.title}"



