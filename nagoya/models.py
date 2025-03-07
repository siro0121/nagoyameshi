from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.db.models import Avg

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
  name = models.CharField(max_length=200)
  category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name="restaurants")
  address = models.TextField(default="No Address Provided")
  opening_time = models.TimeField(null=True, blank=True)
  closing_time = models.TimeField(null=True, blank=True)
  closed_days = models.CharField(max_length=100, blank=True, null=True)
  phone_number = models.CharField(max_length=15, blank=True, null=True)

  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  img = models.ImageField(blank=True, default='noImage.png', upload_to='media/')
  
  

  def __str__(self):
        return self.name

  def average_rating(self):
        avg_rating = self.reviews.aggregate(Avg('rating'))['rating__avg']
        return round(avg_rating, 1) if avg_rating else "評価なし"  # 小数1桁で丸める

 # 新規作成・編集完了時のリダイレクト先
  def get_absolute_url(self):
        return reverse('list')

class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1〜5 の星評価
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.restaurant.name} ({self.rating}★)"

