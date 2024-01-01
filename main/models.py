from django.db import models
from django.utils import timezone


# Create your models here.
class StudentsResgister(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    course_name = models.CharField(max_length=255)
    signup_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}: {self.first_name} {self.last_name} - {self.course_name}"


class contact(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=14, unique=True)
    comments = models.CharField(max_length=700)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.id}: {self.first_name} {self.last_name} - {self.phone}"

    class Meta:
        ordering = ["-date"]
