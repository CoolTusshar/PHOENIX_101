from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from .choices import USER_CHOICES

class Institution(models.Model):
    institution_id = models.IntegerField(primary_key=True)
    institution_name = models.CharField(max_length=140,null=False,default="ABCD")
    institution_address = models.CharField(max_length=150,null=False,default="ALPHA")
    institution_total_rating = models.IntegerField()
    institution_total_raters = models.IntegerField()

class Profile(models.Model):
    user = models.OneToOneField(User)
    school = models.ForeignKey(Institution)
    type = models.IntegerField(choices=USER_CHOICES,blank=False,default=1)


class Feedback(models.Model):
    user_type = models.IntegerField(choices=USER_CHOICES,default=3)
    user_name = models.CharField(max_length=10,primary_key=True,default='tushar')
    answer_list= models.TextField()
