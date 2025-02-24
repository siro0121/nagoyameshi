from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class restaurant(models.Model):
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

 # 新規作成・編集完了時のリダイレクト先
  def get_absolute_url(self):
        return reverse('list')

