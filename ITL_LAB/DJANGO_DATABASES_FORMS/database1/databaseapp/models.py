from django.db import models
from django import forms
# Create your models here.
class lives(models.Model):
    name = models.CharField(max_length=100)
    street=models.CharField(max_length=100)
    city=models.CharField(max_length=100)

class livesform(forms.ModelForm):
    class Meta:
        model=lives
        fields=['name','street','city']

class works(models.Model):
    name = models.ForeignKey(lives, on_delete=models.CASCADE)
    company=models.CharField(max_length=100)
    salary = models.FloatField()

class worksform(forms.ModelForm):
    class Meta:
        model=works
        fields=['name','company','salary']

class companyform(forms.ModelForm):
    class Meta:
        model=works
        fields=['company']

