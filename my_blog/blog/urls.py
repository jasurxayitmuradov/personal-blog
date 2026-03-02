from django.urls import path
from . import views

urlpatterns = [
    path('' , views.home , name="blog_home"),
    path('article/<int:article_id>/' , views.article_detail , name='article_detail'),
    path('dashboard/' , views.dashboard , name='dashboard'),
    path('dashboard/add/' , views.article_add , name = 'article_add'),
    path('dashboard/edit/<int:article_id>/' , views.article_edit , name='article_edit'),
]
