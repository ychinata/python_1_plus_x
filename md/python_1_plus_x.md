# day03

## 知识点

#### MVC模式

#### SSM框架

SSM（Spring+SpringMVC+MyBatis）框架集由Spring、MyBatis两个开源框架整合而成（SpringMVC是Spring中的部分内容），常作为数据源较简单的web项目的框架。

### 图片路径

C:\Users\paidaxinxinxin\Documents\code\codePython\python_1_plus_x\md\data

![00](data\00.png)

### 安装

#### mysql安装

密码为123456

cmd命令行：mysql -u root -p即可进入，不用输入密码，直接回车

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pymysql

#### Django安装

pip install -i https://pypi.tuna.tsinghua.edu.cn/simple django==3.2.8

#### Navicat

![02](data\02.png)

新建数据库:

![03](data\03.png)

#### Postman

#### Apipost

## 上午

### 进度

1.3 创建项目

1.4 定义模型

1.5 后台管理

### 操作

#### 创建工程



django-admin startproject zhonghui 

python manage.py runserver

成功运行Django！

![01](data\01.png)

#### 创建子应用

python manage.py startapp courses



#### 模型迁移

//生成迁移文件

python manage.py makemigrations

如果报以下错：

"'cryptography' package is required for sha256_password or caching_sha2_password auth methods"

可通过安装cryptography来解决： pip install cryptography

//执行迁移

python manage.py migrate

由于我设置了连接数据库不使用密码，所以在文件settings.py里的DATABASES的设置里：

"PASSWORD": '',

迁移成功：

![04](data\04.png)

pycharm的命令行，ctrl+s会重启

#### 创建管理员

python manage.py createsuperuser

用户名设置为hxy, 123@qq.com 密码：123456

登录成功：

![05](data\05.png)

修改admin.py

重启程序：

![06](data\06.png)

// 重置密码

python manage.py change password 用户名

## 下午

### 进度

1.6 视图及URL

1.7 ORM数据库操作

### 操作

#### 视图

配置路由

```python
def index(request):
    return HttpResponse(reverse("courses:index"))
```

反向解析：reverse

courses这里是一个命名空间

访问http://127.0.0.1:8000/courses/index

显示路由反向解析效果如下：

![07](data\07.png)

路由带两个参数：

http://127.0.0.1:8000/courses/index/1/2

![08](data\08.png)

通过form表单进行传参POST的方式，需要将settins.py里的这行注释掉

```python
'django.middleware.csrf.CsrfViewMiddleware',

```

// 通过json提交的参数

json不能使用单引号，只能使用双引号

