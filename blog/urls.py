
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('label/', views.label, name='label'),
    path('archives/<str:arch>', views.archives, name='archives'),
    path('index/<int:pg>', views.index, name='index_num'),
    path('article/<int:article_id>', views.article, name='article'),
    path('hello/', views.hello, name='hello'),
    path('about/', views.about, name='about'),
    path('files/', views.files, name='files'),
]