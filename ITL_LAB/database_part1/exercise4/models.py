from django.db import models
from django import forms


class Exercise4Product(models.Model):
    title = models.CharField(max_length=255)
    price = models.FloatField()
    description = models.TextField()

    def __str__(self):
        return f"{self.title}"


class Exercise4ProductForm(forms.ModelForm):
    class Meta:
        model = Exercise4Product
        fields = ["title", "price", "description"]
