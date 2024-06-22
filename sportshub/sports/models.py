from django.db import models
from django.utils import timezone
import uuid


# Create your models here.
class Event(models.Model):
    img = models.ImageField(upload_to="pic")
    name = models.CharField(max_length=150)
    desc = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Register(models.Model):
    REGISTRATION_PREFIX = 'REG'

    stu_name = models.CharField(max_length=100)
    stu_class = models.CharField(max_length=100)
    stu_rollno = models.CharField(max_length=20)
    name = models.ForeignKey(Event, on_delete=models.CASCADE)
    registration_number = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.stu_name}'s registration for {self.name}"

    def generate_registration_number(self):
        # Generate a unique registration number
        unique_id = uuid.uuid4().hex[:6].upper()
        self.registration_number = f'{self.REGISTRATION_PREFIX}{unique_id}'
