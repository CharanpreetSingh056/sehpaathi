from django.db import models

# Create your models here.
class interview_experiences_db(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    interview_experience=models.TextField(max_length=10000)
    company=models.CharField(max_length=100)
    grad_year=models.IntegerField()
    course=models.CharField(max_length=100)
    date_of_upload=models.DateTimeField(auto_now_add=True) #adds date automatically

    def __str__(self):
        return self.company