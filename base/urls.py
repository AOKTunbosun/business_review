from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('business/', views.business, name='business'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('business/review/<str:pk>/', views.review_form, name='business-review')
]