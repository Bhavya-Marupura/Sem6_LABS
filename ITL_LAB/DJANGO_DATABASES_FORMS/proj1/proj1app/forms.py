from django import forms

class form1(forms.Form):
    name = forms.CharField(label="Enter name",max_length=100)
    roll = forms.CharField(label="Enter roll no",max_length=50)
    choices=[('maths','maths'),('science','science'),('pe','pe'),]
    subject = forms.ChoiceField(label="Select sub", choices=choices)