from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('businesses/', views.businesses, name='businesses'),
    path('business/<str:pk>', views.business_page, name='business-page'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.signup_page, name='signup'),
    path('profile/<str:pk>', views.profile, name='profile')
]