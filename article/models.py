# _*_ coding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models        # 每一个Django Model都继承自Model
from django.core.urlresolvers import reverse
# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length = 100)                  #博客题目
    category = models.CharField(max_length = 50, blank = True)  #博客标签
    date_time = models.DateTimeField(auto_now_add = True)       #博客日期,auto_now_add设置True表示自动设置对象增加时间
    content = models.TextField(blank = True, null = True)       #博客文章正文

    # 获取URL并转换成url的表示格式
    def get_absolute_url(self):
        path = reverse('detail', kwargs={'article_id': self.id})
        return "http://127.0.0.1:8000/home%s" % path


    #python2使用__unicode__, python3使用__str__
    def __unicode__(self) :
        return self.title

    class Meta:  #按时间下降排序
        ordering = ['-date_time']


class UserProfile(models.Model):
    username = models.CharField(verbose_name=u'用户名',max_length = 100)
    email = models.EmailField(verbose_name=u'邮箱',max_length = 50)
    mobile = models.CharField(verbose_name=u'手机号码',max_length=11,null=True)
    gender = models.CharField(verbose_name=u'性别',choices=(('male','男性'),('female','女性')),max_length=6,default='male')
    password = models.CharField(max_length=11,null= True)

    # 获取URL并转换成url的表示格式


    class Meta:
        verbose_name=u'用户信息'
        verbose_name_plural= '用户信息'

    def __unicode__(self):
        return self.username