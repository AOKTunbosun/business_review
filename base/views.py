from django.shortcuts import render, redirect
from .forms import ReviewForm

businesses = [
    {'id': 1, 'name': 'Dalzeem Ventures'},
    {'id': 2, 'name': 'Excellous Services'}
]


# Create your views here.
def home(request):
    return render(request, 'base/home.html')


def business(request):
    context = {'businesses': businesses}
    return render(request, 'base/business.html', context)

def login(request):
    return render(request, 'base/login.html')

def signup(request):
    return render(request, 'base/signup.html')

def review_form(request, pk):
    form = ReviewForm()
    if form.is_valid():
        form.save()
        return redirect('home')

    context = {'form': form}
    return render(request, 'base/review_form.html', context)