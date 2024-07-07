
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Student
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect



def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})



def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})



@login_required
def home(request):
    return render(request, 'registration/home.html')
