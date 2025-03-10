"""
URL configuration for nagoyamesi project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from nagoya import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.top, name='top'),
    path('crud/', views.ProductListView.as_view(), name="list"),
    path('crud/new/', views.ProductCreateView.as_view(), name="new"),
    path('crud/edit/<int:pk>', views.ProductUpdateView.as_view(), name="edit"),
    path('crud/delete/<int:pk>', views.ProductDeleteView.as_view(), name="delete"),
    path('register/', views.register, name='register'),# 新規登録ページ
    path('login/', views.login_view, name='login'),  # ログインページを追加
    path('mypage/', views.mypage, name='mypage'),  # ユーザーページ
    path('logout/', auth_views.LogoutView.as_view(next_page='top'), name='logout'),
    path('restaurant/<int:restaurant_id>/review/', views.add_review, name='add_review'),
    path('restaurant/<int:restaurant_id>/', views.restaurant_detail, name='restaurant_detail'),
    path('restaurants/', views.restaurant_list, name='restaurant_list'),
    path('restaurants/<int:id>/', views.restaurant_detail, name='restaurant_detail'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
