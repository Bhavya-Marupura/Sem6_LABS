from django.shortcuts import render, redirect
from .models import *


def exercise1(request):
    return redirect('exercise1Home')


def exercise1Home(request):
    categories = Exercise1Category.objects.all()
    pages = Exercise1Page.objects.all()
    return render(
        request,
        'exercise1Home.html',
        {'categories': categories, 'pages': pages}
    )


def exercise1CategoryEntry(request):
    if request.method == 'POST':
        form = Exercise1CategoryForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

    form = Exercise1CategoryForm()
    return render(
        request,
        'exercise1CategoryEntry.html',
        {'form': form}
    )


def exercise1PageEntry(request):
    if request.method == 'POST':
        form = Exercise1PageForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

    form = Exercise1PageForm()
    return render(
        request,
        'exercise1PageEntry.html',
        {'form': form}
    )