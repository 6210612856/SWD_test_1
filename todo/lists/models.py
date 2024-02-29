from django.db import models

class ToDoList(models.Model):
    title = models.CharField(max_length=300)
    desc = models.CharField(max_length=1000)
    create_date = models.DateTimeField(auto_now_add=True)