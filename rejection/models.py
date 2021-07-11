from django.db import models

# Create your models here.
class rejection_reasons_db(models.Model):

    name=models.CharField(max_length=100,default="Anonymous")
    email=models.EmailField() # Update krwaane ke lie.
    reason=models.TextField(max_length=1000)
    time_of_upload=models.DateTimeField(auto_now_add=True)
    company=models.CharField(max_length=100,default='None')


    def __str__(self):
        return self.reason

class rejection_reasons_comments_db(models.Model):

    name=models.CharField(max_length=100)
    email=models.EmailField()
    reason=models.ForeignKey(rejection_reasons_db,on_delete=models.CASCADE,related_name='comment')
    comment=models.TextField(max_length=1000)
    time_of_upload=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
