from django.db import models
from django import forms


class Exercise2Lives(models.Model):
    person_name = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)

    def __str__(self):
        return self.person_name


class Exercise2LivesForm(forms.ModelForm):
    class Meta:
        model = Exercise2Lives
        fields = ['person_name', 'street', 'city']


class Exercise2Works(models.Model):
    person_name = models.ForeignKey(Exercise2Lives, on_delete=models.CASCADE)
    company = models.CharField(max_length=255)
    salary = models.FloatField()


class Exercise2WorksForm(forms.ModelForm):
    class Meta:
        model = Exercise2Works
        fields = ['person_name', 'company', 'salary']


class Exercise2CompanyForm(forms.ModelForm):
    class Meta:
        model = Exercise2Works
        fields = ['company']
