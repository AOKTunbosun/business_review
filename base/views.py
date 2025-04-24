from django.shortcuts import render, redirect
from .forms import ReviewForm
from .models import Business, Category
from django.http import HttpResponse

# businesses = [
#     {'id': 1, 'name': 'Dalzeem Ventures'},
#     {'id': 2, 'name': 'Excellous Services'}
# ]


# Create your views here.
def home(request):
    businesses = Business.objects.all()
    categories = Category.objects.all()
    print(businesses)
    context = {'businesses': businesses, 'categories': categories}
    return render(request, 'base/home.html', context)

def businesses(request):
    businesses = Business.objects.all()
    context = {'businesses': businesses}
    return render(request, 'base/businesses.html', context )
    # return HttpResponse('Businesses')


def business_page(request, pk):
    business = Business.objects.get(id=pk)

    context = {'business': business}
    return render(request, 'base/business_page.html', context)

def login_page(request):
    return render(request, 'base/login.html')

def signup_page(request):
    return render(request, 'base/signup.html')

def review_form(request, pk):
    form = ReviewForm()
    if form.is_valid():
        form.save()
        return redirect('home')

    context = {'form': form}
    return render(request, 'base/review_form.html', context)