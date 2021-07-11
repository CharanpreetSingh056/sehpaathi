from django.db import models

# Create your models here.
class questions_db(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    question=models.CharField(max_length=100)
    company=models.CharField(max_length=50)
    year=models.IntegerField()
    similar_question=models.CharField(max_length=1000,default=None)

    def __str__(self):
        return self.company