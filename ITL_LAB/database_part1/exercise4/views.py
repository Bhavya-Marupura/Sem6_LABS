from django.shortcuts import render, redirect
from .models import *


def exercise4(request):
    return redirect('exercise4Home')


def exercise4Home(request):
    products = Exercise4Product.objects.all()
    return render(
        request,
        'exercise4Home.html',
        {'products': products}
    )


def exercise4ProductEntry(request):
    if request.method == 'POST':
        form = Exercise4ProductForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

    form = Exercise4ProductForm()
    return render(
        request,
        'exercise4ProductEntry.html',
        {'form': form}
    )
