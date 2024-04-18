from django.shortcuts import render
from . forms import form1
# Create your views here.

def firstpage(request):
   form=form1()
   if request.method=='POST':
      form=form1(request.POST)
      if form.is_valid():
         name= form.cleaned_data['name']
         roll = form.cleaned_data['roll']
         subject = form.cleaned_data['subject']

   return render(request,'firstpage.html',{'form':form})

def secondpage(request):
   name=request.POST['name']
   roll=request.POST['roll']
   subject=request.POST['subject']
   context={'name':name,'roll':roll,'subject':subject}
   return render(request, 'secondpage.html',context)