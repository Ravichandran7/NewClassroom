from django.db import models
from django.contrib.auth.models import User
import uuid

class Classroom(models.Model):
    name = models.CharField(max_length=100)
    code = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="teacher_classrooms")

    def __str__(self):
        return self.name

class Membership(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'classroom')

    def __str__(self):
        return f"{self.user.username} -> {self.classroom.name}"
