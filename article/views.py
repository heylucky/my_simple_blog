# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.views.generic import View
from django.http import Http404


from models import Article


class ArticleView(View):
    def get(self,request):
        post_list = Article.objects.all()
        return render(request,'home.html',{'post_list': post_list})

    def post(self,request):
        pass


class ArticlePage(View):
    def get(self,request,article_id):
        post = Article.objects.get(pk=article_id)       # 主键pk
        return render(request,'articlepage.html',{'post':post})


class ArchivesView(View):
    def get(self,request):
        try:
            post_list = Article.objects.all()
        except Article.DoesNotExist:
            raise Http404
        return render(request, 'archives.html', {'post_list': post_list,
                                                 'error': False})


def search_tag(request, tag) :
    try:
        post_list = Article.objects.filter(category__iexact = tag) #contains
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'tag.html', {'post_list' : post_list})


class AboutmeView(View):
    def get(self,request):
        return render(request,'aboutme.html',{})