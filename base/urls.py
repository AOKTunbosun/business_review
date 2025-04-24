from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('businesses/', views.businesses, name='businesses'),
    path('business/<str:pk>', views.business_page, name='business-page'),
    path('login/', views.login_page, name='login'),
    path('signup/', views.signup_page, name='signup'),
    path('business/review/<str:pk>/', views.review_form, name='business-review')
]