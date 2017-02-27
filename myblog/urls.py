# _*_ coding:utf-8 _*_
"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView       # 专门用于静态文件

from article.views import ArticleView,ArticlePage,ArchivesView,AboutmeView,LoginView,RegisterView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',ArticleView.as_view(),name='home'),
    url(r'^home/(?P<article_id>\d+)/$', ArticlePage.as_view(), name='detail'),
    url(r'^archives/$', ArchivesView.as_view(), name = 'archives'),
    url(r'^tag/(?P<tag>\w+)/$', 'article.views.search_tag', name = 'search_tag'),
    url(r'^aboutme/$', AboutmeView.as_view(), name = 'aboutme'),
    url(r'^login/$', LoginView.as_view(), name = 'login'),
    url(r'^reg/$', RegisterView.as_view(), name = 'register'),

    # url(r'^search/$','article.views.blog_search', name = 'search'),
]
