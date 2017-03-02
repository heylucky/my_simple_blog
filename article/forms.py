# _*_ coding:utf-8 _*_
__author__ = 'Jack Lin'

from django import forms
# from captcha.fields import CaptchaField     # 验证码


class LoginForm(forms.Form):
    username = forms.CharField(required=True,min_length=2,max_length=30)       # required 表示必填字段
    password = forms.CharField(required=True,min_length=3)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True,min_length=3)
    confirm_password = forms.CharField(required=True, min_length=3)
    username = forms.CharField(required=True,min_length=2,max_length=30)
    # captcha = CaptchaField(error_messages={"invalid":u"lin验证码错误!!!"})


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    # captcha = CaptchaField(error_messages={'invalid':u"lin验证码错误!!!"})

