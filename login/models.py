# coding=utf-8
from __future__ import unicode_literals
# Create your models here.
# login/models.py
from tinymce.models import HTMLField
from django.db import models
class User(models.Model):
    '''用户表'''

    gender = (
        ('male','男'),
        ('female','女'),
    )

    name = models.CharField(max_length=128,unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32,choices=gender,default='男')
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'

class PicTest(models.Model):
    '''上传图片模型 '''
    pic = models.ImageField(upload_to='login/')

class GoodsInfo(models.Model):
    '''富文本模型 '''
    gcontent=HTMLField()
