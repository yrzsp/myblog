# -*- coding:utf-8 -*-
from django.shortcuts import render,get_object_or_404,get_list_or_404
from .models import *
from django.http import HttpResponse
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

def index(request,pg=1):
    blog_all_list = Blog.objects.all()
    paginator = Paginator(blog_all_list, 2)
    page_num = request.GET.get('page',pg)
    page_of_blogs = paginator.get_page(page_num)
    count_list = [int(i) for i in range(1,paginator.num_pages+1)]
    return render(request, 'blog/index.html', {'art_list': page_of_blogs,'page_range':count_list,'now_page':pg})

def article(request,article_id):
    text = get_object_or_404(Blog,pk=article_id)
    context = {
        'title': text.blog_title,
        'label': text.blog_label,
        'alter_date': text.alter_time,
        'article' : text.Content,
    }
    return render(request,'blog/article.html',context)

def hello(request):
    return render(request,'blog/base.html')

def label(request):
    blog_all_list = Blog.objects.all()
    label_list = {}
    for blog in blog_all_list:
        if blog.blog_label in label_list:
            label_list[blog.blog_label] += 1
        else:
            label_list[blog.blog_label] = 1
    return render(request,'blog/label.html',{'label_list':list(label_list.items())})
def archives(request,arch):
    text = get_list_or_404(Blog, blog_label=arch)
    context = {
        'label': arch,
        'archives_list': text,
    }
    return render(request,'blog/archives.html',context)


def about(request):
    return render(request,'blog/about.html')

def files(request):
    text = Blog.objects.all()
    context = {
        'article_list': text,
    }
    return render(request,'blog/files.html',context)