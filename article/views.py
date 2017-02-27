# _*_ coding:utf-8 _*_
from django.shortcuts import render
from django.views.generic import View
from django.http import Http404
from django.core.paginator import PageNotAnInteger,Paginator,EmptyPage
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password       # 对明文密码进行加密
from django.contrib.auth import authenticate,login,logout       # 权限认证 ，登录，退出

from models import Article,UserProfile
from forms import RegisterForm,LoginForm

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


class RegisterView(View):
    def get(self,request):
        return render(request,'register.html',{})

    def post(self,request):
        register_form = RegisterForm(request.POST)
        print "*******************************"
        print register_form
        if register_form.is_valid():
            pwd = request.POST.get("password","")
            pwd2 = request.POST.get("confirm_password", "")
            if pwd != pwd2:
                return render(request, "register.html",{"msg":u"密码不一致"})

            user_name = request.POST.get("email", "")  # 值“”默认是空,此时获取的user_name为邮箱地址
            if UserProfile.objects.filter(email=user_name):
                return render(request,"register.html",{"register_form": register_form,"msg":"用户已存在!!!"})
            pass_word = request.POST.get("password", "")
            user_profile = UserProfile()
            user_profile.username = user_name       # user_name 默认为邮箱
            user_profile.email = user_name
            # user_profile.is_active = False
            # user_profile.password = make_password(pass_word)
            user_profile.password = make_password(pass_word)
            user_profile.save()             # 保存到数据库当中。
            return render(request,"login.html")
        else:
            return render(request,"register.html",{"register_form":register_form})  # 见html中register_form.errors.email/password; register_form.errors.items




class LoginView(View):
    def get(self,request):
        return render(request,'login.html',{})

    def post(self,request):
        login_form=LoginForm(request.POST)
        if login_form.is_valid():       # 实际是检查_errors是否为空，为空说明正常,与数据库对比
            username = request.POST.get("username", "")  # 值“”默认是空
            password = request.POST.get("password", "")
            user = authenticate(username=username, password=password)  # 形参是固定的不能修改
            if user is not None:
                # if user.is_active:
                    login(request, user)  # 完成login登录,下面跳到首页
                    return render(request, "home.html", {})   # 跳到首页
                # else:
                #     return render(request,"login.html",{"msg":"用户未激活"})
            else:
                # if user.is_active:
                #     return render(request,"login.html",{"msg":"用户名或密码出错"})
                # else:
                return render(request,"login.html",{"msg":"用户名或密码出错"})
        else:
            return render(request, "login.html",{"login_form" : login_form})