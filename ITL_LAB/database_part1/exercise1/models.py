from django.db import models
from django import forms


class Exercise1Category(models.Model):
    name = models.CharField(max_length=255)
    number_of_visits = models.IntegerField()
    number_of_likes = models.IntegerField()

    def __str__(self):
        return f"{self.name}"


class Exercise1CategoryForm(forms.ModelForm):
    class Meta:
        model = Exercise1Category
        fields = ['name', 'number_of_visits', 'number_of_likes']


class Exercise1Page(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Exercise1Category, on_delete=models.CASCADE)
    url = models.URLField()
    views = models.IntegerField()


class Exercise1PageForm(forms.ModelForm):
    class Meta:
        model = Exercise1Page
        fields = ['category', 'title', 'url', 'views']

