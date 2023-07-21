from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django import forms

class Employ(models.Model):  
    status_choices = [
        ('Approved' , 'Approved'),
        ('Reject' , 'Reject'),
        ('Screen Reject ' , 'Screen Reject'),
        ('Shortlisted','Shortlisted'),
        ('Hold','Hold')
    ]
    passport_choices = [
        ('Yes' , '✅'),
        ('No' , '❌')
    ]


    Name = models.CharField(max_length=100)  
    Skill = models.CharField(max_length=100,blank=True)
    Experience = models.CharField(max_length=100,blank=True)
    Relevant_Experience = models.CharField(max_length=100,blank=True)
    Company = models.CharField(max_length=100,blank=True)
    Availability = models.CharField(max_length=100,blank=True)
    Offer = models.CharField(max_length=100,blank=True)
    CTC = models.CharField(max_length=100,blank=True)
    ECTC = models.CharField(max_length=100,blank=True)
    Location = models.CharField(max_length=100,blank=True)
    Contact	= models.CharField(max_length=100,unique=True)
    Mail_id = models.EmailField(unique=True)
    Reason_for_job_change = models.CharField(max_length=100,blank=True)
    Resume = models.FileField(blank=True, null=True)
    PassPort = models.CharField(max_length=50 , 
    choices=passport_choices,blank=True)
    status = models.CharField(max_length=50 ,  
    choices=status_choices, blank=True)
    user  = models.ForeignKey(User, on_delete= models.CASCADE)
    Date = models.DateTimeField(auto_now_add=True)

class Record(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class RejectedEmploy(models.Model):
    status_choices = [
        ('Approved' , 'Approved'),
        ('Reject' , 'Reject'),
        ('Screen Reject ' , 'Screen Reject'),
        ('Shortlisted','Shortlisted'),
        ('Hold','Hold')
    ]
    passport_choices = [
        ('Yes' , '✅'),
        ('No' , '❌')
    ]


    Name = models.CharField(max_length=100)
    Skill = models.CharField(max_length=100, blank=True)
    Experience = models.CharField(max_length=100, blank=True)
    Relevant_Experience = models.CharField(max_length=100, blank=True)
    Company = models.CharField(max_length=100, blank=True)
    Availability = models.CharField(max_length=100, blank=True)
    Offer = models.CharField(max_length=100, blank=True)
    CTC = models.CharField(max_length=100, blank=True)
    ECTC = models.CharField(max_length=100, blank=True)
    Location = models.CharField(max_length=100, blank=True)
    Contact = models.CharField(max_length=100, unique=True)
    Mail_id = models.EmailField(unique=True)
    Reason_for_job_change = models.CharField(max_length=100, blank=True)
    Resume = models.FileField(blank=True, null=True)
    PassPort = models.CharField(max_length=50, choices=passport_choices, blank=True)
    status = models.CharField(max_length=50, choices=status_choices, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Date = models.DateTimeField(auto_now_add=True)