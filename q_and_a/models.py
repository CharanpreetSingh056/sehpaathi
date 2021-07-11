from django.db import models

# Create your models here.
class general_questions_db(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    time_of_upload=models.DateTimeField(auto_now_add=True)
    question=models.TextField(max_length=1000)


    def __str__(self):
        return self.email

class answers_db(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    time_of_upload=models.DateTimeField(auto_now_add=True)
    answer=models.TextField(max_length=1000)
    question=models.ForeignKey(general_questions_db,on_delete=models.CASCADE,related_name='answer')

    def __str__(self):
        return self.email