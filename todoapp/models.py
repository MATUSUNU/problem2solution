from django.db import models


class Task(models.Model):
    content = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content[:15] + ("..." if len(self.content) > 15 else "")

    @property
    def short_content(self):
        return self.content[:25] + ("..." if len(self.content) > 25 else "")

    class Meta:
        ordering = ["-updatedAt"]
        verbose_name = "Task"
        verbose_name_plural = "Tasks"
