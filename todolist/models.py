from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self) -> str:
        return self.name


class Task(models.Model):
    content = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True,blank=True)
    is_done = models.BooleanField()
    tags = models.ManyToManyField(
        to=Tag,
        blank=True,
        related_name="tasks"
    )

    def __str__(self) -> str:
        return f"{self.content} created on {self.datetime}"
