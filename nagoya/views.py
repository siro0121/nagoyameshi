from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Restaurant, Review
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from django.db.models import Avg


class TopView(TemplateView):
    model = Restaurant
    template_name = "top.html"

class ProductListView(ListView):
    model = Restaurant
    template_name = "list.html"

class ProductCreateView(CreateView):
    model = Restaurant
    fields = '__all__'

class ProductUpdateView(UpdateView):
    model = Restaurant
    fields = '__all__'
    template_name_suffix = '_update_form'

class ProductDeleteView(DeleteView):
    model = Restaurant
    template_name = "nagoya/restaurant_confirm_delete.html"
    success_url = reverse_lazy('list')



def top(request):
    restaurants = Restaurant.objects.annotate(average_rating=Avg('reviews__rating')).order_by('-average_rating')[:5]  # ★5件に制限
    for r in restaurants:
        if r.average_rating is None:
            r.average_rating = 0  # レビューがない場合は0にする
        r.star_percentage = r.average_rating * 20  # ★の割合 (5段階評価なので100% = 5×20)
    
    return render(request, 'top.html', {'restaurants': restaurants})

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "このユーザー名は既に使われています。")
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            login(request, user)  # 登録後に自動ログイン
            return redirect('top')  # TOPページにリダイレクト

    return render(request, 'nagoyamesi/register.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('top')  # ログイン後にTOPページへ
        else:
            messages.error(request, "ユーザー名またはパスワードが間違っています")

    return render(request, 'nagoyamesi/login.html')

@login_required 

def mypage(request):
    return render(request, 'mypage.html', {'user': request.user})

#レビュー
@login_required
def add_review(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.restaurant = restaurant
            review.user = request.user
            review.save()
            return redirect('restaurant_detail', restaurant_id=restaurant.id)  # レストラン詳細ページへリダイレクト
    else:
        form = ReviewForm()

    return render(request, 'add_review.html', {'form': form, 'restaurant': restaurant})

def restaurant_detail(request, id):
    restaurant = get_object_or_404(Restaurant, id=id)
    reviews = restaurant.reviews.all()  
    return render(request, 'restaurant_detail.html', {'restaurant': restaurant, 'reviews': reviews})


def restaurant_list(request):
    # すべての店舗情報を取得
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurant_list.html', {'restaurants': restaurants})

def search_results(request):
    query = request.GET.get('q')
    results = Restaurant.objects.filter(name__icontains=query) if query else []

    return render(request, 'restaurant_list', {
        'query': query,
        'results': results
    })
