# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.views.generic import View
from django.http import Http404
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage


from models import Article


class ArticleView(View):
    def get(self,request):
        posts = Article.objects.all()
        paginator = Paginator(posts,3)
        page = request.GET.get('page')      # 从 Http 请求中获取用户请求的页码号

        try:
            post_list = paginator.page(page)  # 根据页码号获取第几页的数据
        except PageNotAnInteger:
            # 异常处理，如果用户传递的page值不是整数，则把第一页的值返回给他
            post_list = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            post_list = paginator.page(paginator.num_pages)      # paginator.num_pages :页面总数

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


def search_tag(request, tag):
    try:
        post_list = Article.objects.filter(category__iexact = tag) #contains
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'tag.html', {'post_list' : post_list})


class AboutmeView(View):
    def get(self,request):
        return render(request,'aboutme.html',{})