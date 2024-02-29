from django.shortcuts import render
from django.http import HttpResponse
from solved2app.forms import LoginForm

def formView(request):
    if request.session.has_key('username'):
        username = request.session['username']
        return render(request, 'loggedin.html', {"username": username})
    else:
        return render(request, 'login.html', {})


def login(request):
    username = 'not logged in'
    if request.method == 'POST':
        MyLoginForm = LoginForm(request.POST)
        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['username']
            request.session['username'] = username
        else:
            MyLoginForm = LoginForm()
    return render(request, 'loggedin.html', {"username": username})

def logout(request):
    try:
        del request.session['username']
    except KeyError:
        pass
    return HttpResponse("<strong>You are logged out.</strong>")

