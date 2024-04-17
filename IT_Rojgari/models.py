from django.db import models


# Create your models here.
class JobPosting(models.Model):
    # id -> 1 by default and auto incremenrs
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=20)
    description = models.TextField()
    company = models.TextField(max_length=100)
    salery = models.IntegerField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} | {self.company} | Active: {self.is_active}"


# models manager -> objects
