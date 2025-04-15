from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.TextField()


class Business(models.Model):
    business_id = models.AutoField(primary_key=True)
    business_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    address = models.TextField(null=False, blank=False)
    city = models.CharField(max_length=30, null=False, blank=False)
    contact = models.IntegerField(null=True)
    contact_mail = models.TextField(null=False, blank=False)
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    business_id = models.ForeignKey(Business, on_delete=models.CASCADE)
    rating = models.IntegerField(null=False)
    review_text = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)


# class BusinessImage(models.Model):
#     image_id = models.AutoField(primary_key=True)
#     business_id = models.ForeignKey(Business, on_delete=models.CASCADE)
#     image_url = models.ImageField(upload_to='business_images/uploaded')
#     uploaded_at = models.DateTimeField(auto_now_add=True)

class ReviewLike(models.Model):
    like_id = models.AutoField(primary_key=True)
    review_id = models.ForeignKey(Review, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_at = models.DateTimeField(auto_now_add=True)


class Response(models.Model):
    response_id = models.AutoField(primary_key=True)
    review_id =models.ForeignKey(Review, on_delete=models.CASCADE)
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    response_text = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
