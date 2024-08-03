from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import datetime
# Create your models here.

class frist_model(models.Model):
    name = models.CharField(max_length=30)
    age = models.PositiveIntegerField()
    email = models.EmailField()
    
    def __str__(self):
        return self.name
        
    
class second_model(models.Model):
    name = models.CharField(max_length=30)
    institute = models.CharField(max_length=50)
    start_year = models.PositiveIntegerField()

    def __str__(self):
        return self.institute



class thirth_model(models.Model):
    # GENDER_CHOICES=[
    #     ('Male','Male'),
    #     ('Female','Female'),
    #     ('Others','Others')
    # ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank=True)
    title = models.CharField(max_length=30 , null =True, blank = True)
    phone = models.PositiveIntegerField(null=True,blank=True)
    email = models.EmailField(null = True, blank = True)
    address = models.CharField(max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=50, null=True, blank=True)
    # create_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title



class fourth_model(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank=True)
    title = models.CharField(max_length=50, null=True,blank=True)
    salary=models.PositiveIntegerField()
    city=models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    class_in = models.CharField(max_length=50)
    create_at = models.DateTimeField(default=datetime.now)
    def __str__(self):
        return self.title