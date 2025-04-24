from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name



class Business(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    description = models.TextField(null=True)
    address = models.TextField(null=False, blank=False)
    city = models.CharField(max_length=30, null=False, blank=False)
    contact = models.BigIntegerField(null=True)
    contact_mail = models.TextField(null=False, blank=False)
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Review(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    business_id = models.ForeignKey(Business, on_delete=models.CASCADE)
    rating = models.IntegerField(null=False)
    review_text = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.review_id


# class BusinessImage(models.Model):
#     id = models.AutoField(primary_key=True)
#     business_id = models.ForeignKey(Business, on_delete=models.CASCADE)
#     image_url = models.ImageField(upload_to='business_images/uploaded')
#     uploaded_at = models.DateTimeField(auto_now_add=True)

class ReviewLike(models.Model):
    id = models.AutoField(primary_key=True)
    review_id = models.ForeignKey(Review, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.like_id


class Response(models.Model):
    id = models.AutoField(primary_key=True)
    review_id =models.ForeignKey(Review, on_delete=models.CASCADE)
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    response_text = models.TextField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return self.response_id
