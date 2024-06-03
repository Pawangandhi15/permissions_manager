from django.db import models

class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.task_name}"