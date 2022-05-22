# -*- coding: utf-8 -*-
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


GENDER_CHOICES = (
    ("male", "男"),
    ("female", "女")
)


class BaseModel(models.Model):
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        # 如果我们不想让模型生成数据表，就把他定义为一个抽象模型类
        abstract = True


# Create your models here.
class UserPro(AbstractUser):
    nickname = models.CharField(max_length=50, default="", verbose_name="昵称")
    birthday = models.DateField(null=True, blank=True, verbose_name="生日")
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, verbose_name="性别")
    address = models.CharField(max_length=100, default="", verbose_name="地址")
    image = models.ImageField(upload_to="user_image/", default="default.jpg", verbose_name="用户头像")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname if self.nickname else self.username


class Star(BaseModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, verbose_name="姓名")
    age = models.IntegerField(verbose_name="年龄")
    sex = models.CharField(max_length=10, verbose_name="性别")
    avatar = models.ImageField(upload_to="images/", verbose_name="头像")
    personal = models.TextField(verbose_name="个人简介")
    profession = models.CharField(max_length=50, verbose_name="职业")

    class Meta:
        verbose_name = "明星"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
