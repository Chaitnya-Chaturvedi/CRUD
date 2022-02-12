import email
from unicodedata import name
from django.shortcuts import redirect, render
from .forms import UserForm
from .models import User
# Create your views here.

def add_show(request):
    if request.method == "POST":
        fm = UserForm(request.POST)
        if fm.is_valid():
            nm= fm.cleaned_data['name']
            em= fm.cleaned_data['email']
            ps= fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=ps)
            reg.save()
            return redirect('show')
    else:
        fm = UserForm()
    return render(request, 'enroll/show.html', {'form':fm})
