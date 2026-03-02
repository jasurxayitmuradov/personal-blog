from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import ArticleForm

def home(request):
    articles = Article.objects.all().order_by('-pub_date')
    return render(request, 'blog/home.html', {'articles': articles})

def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'blog/article_detail.html', {'article': article})

def dashboard(request):
    articles = Article.objects.all().order_by('-pub_date')
    return render(request, 'blog/dashboard.html', {'articles': articles})

def article_add(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        
        form = ArticleForm()
    
    
    return render(request, 'blog/article_form.html', {'form': form, 'title': 'Add New Article'})

def article_edit(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if request.method == "POST":
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        
        form = ArticleForm(instance=article)
    
    return render(request, 'blog/article_form.html', {'form': form, 'title': 'Edit Article'})