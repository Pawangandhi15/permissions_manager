from django.db import models

class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.project_name}"

