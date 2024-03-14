from django.shortcuts import render, redirect
from .models import *


def exercise3(request):
    return redirect('exercise3Home')


def exercise3Home(request):
    authors = Exercise3Author.objects.all()
    publishers = Exercise3Publisher.objects.all()
    books = Exercise3Book.objects.all()
    return render(
        request,
        'exercise3Home.html',
        {'authors': authors, 'publishers': publishers, 'books': books}
    )


def exercise3AuthorEntry(request):
    if request.method == 'POST':
        form = Exercise3AuthorForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

    form = Exercise3AuthorForm()
    return render(
        request,
        'exercise3AuthorEntry.html',
        {'form': form}
    )


def exercise3PublisherEntry(request):
    if request.method == 'POST':
        form = Exercise3PublisherForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

    form = Exercise3PublisherForm()
    return render(
        request,
        'exercise3PublisherEntry.html',
        {'form': form}
    )


def exercise3BookEntry(request):
    if request.method == 'POST':
        form = Exercise3BookForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

    form = Exercise3BookForm()
    return render(
        request,
        'exercise3BookEntry.html',
        {'form': form}
    )
