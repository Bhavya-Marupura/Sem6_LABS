from django.db import models
from django import forms


class Exercise3Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Exercise3AuthorForm(forms.ModelForm):
    class Meta:
        model = Exercise3Author
        fields = ["first_name", "last_name", "email"]


class Exercise3Publisher(models.Model):
    name = models.CharField(max_length=255)
    street_address = models.TextField()
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    web_site = models.URLField()

    def __str__(self):
        return f"{self.name}, {self.country}"


class Exercise3PublisherForm(forms.ModelForm):
    class Meta:
        model = Exercise3Publisher
        fields = ["name", "street_address", "city", "state", "country", "web_site"]


class Exercise3Book(models.Model):
    title = models.CharField(max_length=255)
    publication_date = models.DateField()
    authors = models.ManyToManyField(Exercise3Author)
    publisher = models.ForeignKey(Exercise3Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"


class Exercise3BookForm(forms.ModelForm):
    class Meta:
        model = Exercise3Book
        fields = ["title", "publication_date", "authors", "publisher"]
