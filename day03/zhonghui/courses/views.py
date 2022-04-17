import json
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.core import serializers
from django.db.models import Q, F, Max, Min, Avg, Sum

from .models import Teacher, Student, Course

# Create your views here.
# 定义一个视图函数，视图函数至少有一个参数，这个参数用来接收请求对象
# 视图函数要返回一个HttpResponse对象
def index1(request):
    return HttpResponse(reverse("courses:index"))


# url传参
# 修改courses/urls.py
def index2(request, v1, v2):
    return HttpResponse(f"视图函数接收到的参数有：{v1}和{v2}")


# index?name=lisa&age=20
def index3(request):
    name = request.GET.get("name", "")
    age = request.GET.get("age", 0)
    user = {"name": name, "age": age}
    # return HttpResponse(f"视图函数接收到的参数有：姓名：{name}, 年龄：{age}")
    # 序列化
    # json_data = json.dumps(user)
    # return HttpResponse(json_data, content_type="application/json", status=404)
    # 如果不想使用JSON模块进行序列化可以使用JsonResponse对象
    return JsonResponse(user)


# 通过form表单提交的参数
def index4(request):
    name = request.POST.get("name", "")
    age = request.POST.get("age", 0)
    return HttpResponse(f"视图函数接收到的参数有：姓名：{name}, 年龄：{age}")


# 通过json提交的参数
def index5(request):
    # 序列化：就是把Python的数据类型转换为JSON字符串
    # 反序列化：就是把JSON字符串转换为Python数据类型
    # 要对JSON数据进行反序列化
    req_data = json.loads(request.body)
    name = req_data["name"]
    age = req_data["age"]
    return HttpResponse(f"视图函数接收到的参数有：姓名：{name}, 年龄：{age}")


def index6(request):
    # 查询所有的教师, 结果它是一个QuerySet对象，可以进行切片操作
    teachers = Teacher.objects.all()
    # 查询第一个老师
    teacher = Teacher.objects.all()[:1]
    print(teacher)
    # 查看ORM生成的SQL语句
    print(teachers.query)
    print(teacher.query)
    # 对结果进行序列化
    json_data = serializers.serialize("json", teachers)
    return HttpResponse(json_data, content_type="application/json")


def index7(request):
    # 根据老师的姓名查询，get查询结果是一个模型对象
    # teacher = Teacher.objects.get(nickname="娃哈哈")
    # filter查询结果是一个QuerySet对象
    teacher = Teacher.objects.filter(nickname="娃哈哈")
    print(teacher)
    return HttpResponse("ok")


def index8(request):
    # 查询粉丝数量大于等于
    # teachers = Teacher.objects.filter(fans__gte=10000)
    # json_data = serializers.serialize("json", teachers)
    # in查询
    teachers = Teacher.objects.filter(fans__in=[10000, 12000])
    json_data = serializers.serialize("json", teachers)
    return HttpResponse(json_data, content_type="application/json")


def index9(request):
    # 根据粉丝数量进行降序排序
    teachers = Teacher.objects.all().order_by("-fans")
    json_data = serializers.serialize("json", teachers)
    return HttpResponse(json_data, content_type="application/json")


def index10(request):
    # 一对一查询， 多对一查询
    courses = Course.objects.all().select_related("teacher")
    # 遍历
    for course in courses:
        print(course.title, course.teacher.nickname, course.teacher.fans)
    return HttpResponse("ok")


def index11(request):
    # 一对多， 多对多
    students = Student.objects.filter(nickname="昆凌").prefetch_related("course")
    # 获取学生的课程
    for s in students:
        print(s.course.all())
    return HttpResponse("ok")


def index12(request):
    # 反向查询
    print(Teacher.objects.get(nickname="刘德华").course_set.all())
    return HttpResponse("ok")


def index13(request):
    # 查询粉丝数量在10000-12000之间
    teachers = Teacher.objects.filter(Q(fans__gte=1000) & Q(fans__lte=12000))
    json_data = serializers.serialize("json", teachers)
    return HttpResponse(json_data, content_type="application/json")


def index14(request):
    # 活动期间所有课程价格-100
    Course.objects.update(price=F("price") - 100)
    return HttpResponse("ok")


def index15(request):
    # 统计老师的人数
    print(Teacher.objects.all().count())
    # 判断对象是否存在
    print(Teacher.objects.filter(nickname="lisa").exists())
    # 聚合操作：最大值、最小值、平均值、和
    print(Course.objects.aggregate(Max("price"), Min("price"), Avg("price"), Sum("price")))
    return HttpResponse("ok")


def index(request):
    teachers = Teacher.objects.all()
    return render(request, "teachers.html", {"teachers": teachers})


def create(request):
    if request.method == "POST":
        # 获取数据
        nickname = request.POST.get("nickname", "")
        introduce = request.POST.get("introduce", "")
        fans = request.POST.get("fans", "")
        # 实例化一个模型对象
        teacher = Teacher()
        teacher.nickname = nickname
        teacher.introduction = introduce
        teacher.fans = int(fans)
        # 保存对象
        teacher.save()
        return redirect(reverse("courses:index"))
    return render(request, "add.html")


def update(request, name):
    # 判断提交方式
    if request.method == "GET":
        # 把需要更新的老师信息查询出来
        teacher = Teacher.objects.filter(nickname=name)
        return render(request, "update.html", {"teacher": teacher[0]})
    if request.method == "POST":
        # 获取数据
        introduce = request.POST.get("introduce", "")
        fans = request.POST.get("fans", 0)
        # 更新数据
        Teacher.objects.filter(nickname=name).update(
            introduction=introduce,
            fans=int(fans)
        )
        return redirect(reverse("courses:index"))


def delete(request, name):
    # 根据名字查询对象
    teacher = Teacher.objects.filter(nickname=name)
    if teacher:
        # 删除对象
        teacher.delete()
    return redirect(reverse("courses:index"))

