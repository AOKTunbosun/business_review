from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Business, Category, Review
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse


# businesses = [
#     {'id': 1, 'name': 'Dalzeem Ventures'},
#     {'id': 2, 'name': 'Excellous Services'}
# ]


# Create your views here.
def home(request):
    reviews = Review.objects.all()
    businesses = Business.objects.all()
    categories = Category.objects.all()
    # print(reviews)
    context = {'businesses': businesses, 'categories': categories, 'reviews': reviews}
    return render(request, 'base/home.html', context)


def businesses(request):
    categories = Category.objects.all()
    b = request.GET.get('b') if request.GET.get('b') != None else ''
    l = request.GET.get('l') if request.GET.get('l') != None else ''

    if b != '' and l != '':
        businesses = Business.objects.filter(
            Q(name__icontains=b) |
            Q(category__name__icontains=b) |
            Q(address__icontains=l) |
            Q(city__icontains=l)
        )

    elif b != '' and l == '':
        businesses = Business.objects.filter(
            Q(name__icontains=b) |
            Q(category__name__icontains=b)
        )

    elif b == '' and l != '':
        businesses = Business.objects.filter(
            Q(address__icontains=l) |
            Q(city__icontains=l)
        )

    else:
        businesses = Business.objects.filter()

    context = {'businesses': businesses, 'categories': categories}
    return render(request, 'base/businesses.html', context)

def business_page(request, pk):
    business = Business.objects.get(id=pk)

    context = {'business': business}
    return render(request, 'base/business_page.html', context)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)

        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Password is incorrect')

    context = {}
    return render(request, 'base/login.html', context)


def logout_user(request):
    logout(request)
    return redirect('home')


def signup_page(request):
    return render(request, 'base/signup.html')


def review_form(request, pk):
    form = ReviewForm()
    if form.is_valid():
        form.save()
        return redirect('home')

    context = {'form': form}
    return render(request, 'base/review_form.html', context)
