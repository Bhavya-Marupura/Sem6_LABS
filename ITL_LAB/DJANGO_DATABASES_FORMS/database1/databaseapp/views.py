from django.shortcuts import render
from . models import *
# Create your views here.
def home(request):
    return render(request,'home.html',context={})

def livesentry(request):
    form=livesform()
    if request.method=='POST':
        form=livesform(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
    return render(request,'livesentry.html',{'form':form})

def worksentry(request):
    form=worksform()
    if request.method=='POST':
        form=worksform(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            salary=form.cleaned_data['salary']
            if salary>50000:
                return render(request,'alert.html',{'salary':salary})
    return render(request,'worksentry.html',{'form':form})

def display(request):
    living = lives.objects.all()
    working= works.objects.all()
    return render(request,'display.html',{'living':living,'working':working})

def companyemployees(request):
    form=companyform()
    if request.method == 'POST':
        form = companyform(request.POST)
        if form.is_valid():
            company = form.cleaned_data['company']
            living = lives.objects.filter(works__company=company)
            return render(request,'companydisplay.html',{'company': company, 'living': living})
    return render(
        request,
        'companyform.html',
        {'form': form}
    )
def updaterow(request,pk):
    temp=lives.objects.get(pk=pk)
    form=livesform(instance=temp)
    if request.method == 'POST':
        form = livesform(request.POST, instance=temp)
        if form.is_valid():
            form.save()
    return render(request, 'update.html',{'form':form})

def deleterow(request,pk):
    temp=lives.objects.get(pk=pk)
    temp.delete()
    return render(request,'home.html',context={})

