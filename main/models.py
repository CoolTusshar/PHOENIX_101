from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from .choices import INSTITUTION_CHOICES,USER_CHOICES

class Institution(models.Model):
    institution_id = models.IntegerField(primary_key=True)
    institution_name = models.CharField(max_length=140,null=False,default="ABCD")
    institution_type = models.IntegerField(choices=INSTITUTION_CHOICES)
    institution_address = models.CharField(max_length=150,null=False,default="ALPHA")
    institution_total_rating = models.IntegerField()
    institution_total_raters = models.IntegerField()

class Faculty(models.Model):
    faculty_id = models.IntegerField(primary_key=True)
    faculty_name = models.CharField(max_length=140,null=False,default="XYZ")
    faculty_total_rating = models.IntegerField()
    faculty_total_raters = models.IntegerField()
    faculty_contact = models.BigIntegerField()
    faculty_institution = models.ForeignKey(Institution, on_delete=models.CASCADE)

class Student(models.Model):
    student_id = models.IntegerField(primary_key=True)
    student_name = models.CharField(max_length=140,null=False,default="XYZ")
    student_total_rating = models.IntegerField()
    student_total_raters = models.IntegerField()
    student_contact = models.BigIntegerField()
    student_institution = models.ForeignKey(Institution, on_delete=models.CASCADE)

class  Question_List(models.Model):
    type = models.IntegerField()
    qn = models.IntegerField()
    que = models.TextField(max_length=200)

class Feedback(models.Model):
    user_type = models.IntegerField(choices=USER_CHOICES,default=3)
    user_id = models.IntegerField()
    answer_list= models.TextField()
