from django.db import models

class Task(models.Model):
        user = models.ForeignKey("todolist.User", on_delete=models.CASCADE)
        date = models.DateField()
        title = models.CharField(max_length=255)
        description = models.TextField()

class User(models.Model):
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)
        email = models.EmailField()
