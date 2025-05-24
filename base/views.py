from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Business, Category, Review
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.hashers import make_password


# Create your views here.
def home(request):
    reviews = Review.objects.all()
    businesses = Business.objects.all()
    categories = Category.objects.all()

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
    if request.method == 'POST':
        user = request.user
        business_id = pk
        rating = request.POST.get("rating")
        review_text = request.POST.get("review_text")

        # print(user)
        # print(business_id)
        # print(rating)
        # print(review_text)

        try:
            user = User.objects.get(username=user)

        except:
            messages.error(request, 'User does not exist')

        user = get_object_or_404(User, username=user)
        business = get_object_or_404(Business, id=business_id)

        review = Review()
        review.user = user
        review.business = business
        review.rating = rating
        review.review_text = review_text
        review.save()

        return redirect(request.META.get('HTTP_REFERER', '/'))


    business = Business.objects.get(id=pk)
    review = Review.objects.filter(business_id=business.id)

    context = {'business': business, 'review': review}
    return render(request, 'base/business_page.html', context)


def login_page(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            logout(request)

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
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')

        user = User.objects.create_user(username=username, email=email, password=password)

        login(request, user)
        return redirect('home')

    return render(request, 'base/signup.html')


def profile(request, pk):
    user = User.objects.get(id=pk)

    context = {'user': user}
    return render(request, 'base/profile.html', context)

