from django.db import models


# Create your models here.
class Teacher(models.Model):
    """类会被映射为一张表，一个类属性会被映射为一个字段"""
    nickname = models.CharField(max_length=30, primary_key=True, db_index=True, verbose_name="昵称")
    introduction = models.TextField(default="这位老师没有简介", verbose_name="简介")
    fans = models.PositiveIntegerField(default=0, verbose_name="粉丝")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        db_table = "teacher"
        verbose_name = "教师信息表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname


class Course(models.Model):
    """课程信息表"""
    title = models.CharField(max_length=100, primary_key=True, db_index=True, verbose_name="课程名")
    # on_delete=models.CASCADE删除级联
    teacher = models.ForeignKey(Teacher, null=True, blank=True, on_delete=models.CASCADE,
                                verbose_name="教师")
    type = models.SmallIntegerField(choices=((1, "后端开发"), (2, "人工智能"), (3, "数据挖掘"), (0, "其它")),
                                    default=0, verbose_name="课程类型")
    price = models.PositiveIntegerField(verbose_name="价格")
    volume = models.BigIntegerField(verbose_name="销量")
    online = models.DateField(verbose_name="上线时间")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="上传时间")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        db_table = "course"
        verbose_name = "课程信息表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Student(models.Model):
    """学生信息表"""
    nickname = models.CharField(max_length=30, primary_key=True, db_index=True, verbose_name="姓名")
    # 学生和课程是多对多
    course = models.ManyToManyField(Course, verbose_name="课程")
    age = models.PositiveSmallIntegerField(verbose_name="年龄")
    gender = models.SmallIntegerField(choices=((1, "男"), (2, "女"), (0, "保密")),
                                      default=0, verbose_name="性别")
    study_time = models.PositiveIntegerField(default=0, verbose_name="学习时长")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        db_table = "student"
        ordering = ["age"]
        verbose_name = "学生信息表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname


class TeacherAssistant(models.Model):
    """助教信息表"""
    nickname = models.CharField(max_length=30, primary_key=True, db_index=True, verbose_name="昵称")
    # 一对一, on_delete=models.SET_NULL删除置空
    teacher = models.OneToOneField(Teacher, null=True, blank=True, on_delete=models.SET_NULL,
                                   verbose_name="教师")
    hobby = models.CharField(max_length=100, null=True, blank=True, verbose_name="爱好")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    updated_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        db_table = "teacher_assistant"
        verbose_name = "助教信息表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.nickname


