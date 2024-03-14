from django.shortcuts import render, redirect
from .models import *


def exercise2(request):
    return redirect('exercise2Home')


def exercise2Home(request):
    lives = Exercise2Lives.objects.all()
    works = Exercise2Works.objects.all()
    return render(
        request,
        'exercise2Home.html',
        {'lives': lives, 'works': works}
    )


def exercise2LivesEntry(request):
    if request.method == 'POST':
        form = Exercise2LivesForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

    form = Exercise2LivesForm()
    return render(
        request,
        'exercise2LivesEntry.html',
        {'form': form}
    )


def exercise2WorksEntry(request):
    if request.method == 'POST':
        form = Exercise2WorksForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

    form = Exercise2WorksForm()
    return render(
        request,
        'exercise2WorksEntry.html',
        {'form': form}
    )


def exercise2CompanyEmployees(request):
    if request.method == 'POST':
        form = Exercise2CompanyForm(request.POST)
        if form.is_valid():
            company = form.cleaned_data['company']
            lives = Exercise2Lives.objects.filter(exercise2works__company=company)
            return render(
                request,
                'exercise2CompanyEmployees.html',
                {'company': company, 'lives': lives}
            )

    form = Exercise2CompanyForm()
    return render(
        request,
        'exercise2CompanyForm.html',
        {'form': form}
    )