from django import forms

from .models import UserPro


class SearchForm(forms.Form):
    # 验证提交的明星姓名，必须包含内容，最小长度是2
    name = forms.CharField(required=True, min_length=2)


class RegisterForm(forms.Form):
    nickname = forms.CharField(required=True, min_length=2, max_length=10)
    email = forms.EmailField(required=True, min_length=6, max_length=18)
    password = forms.CharField(required=True, min_length=6)

    # 一个邮箱只能注册一个用户
    def clean_email(self):
        email = self.data.get("email")
        user = UserPro.objects.filter(email=email)
        if user:
            raise forms.ValidationError("该邮箱已被注册")
        return email

    def clean_nickname(self):
        nickname = self.data.get("nickname")
        user = UserPro.objects.filter(nickname=nickname)
        if user:
            raise forms.ValidationError("该昵称已被使用")
        return nickname

class LoginForm(forms.Form):
    # 校验用户名或者邮箱
    username = forms.CharField(required=True, min_length=2, max_length=20)
    # 校验密码
    password = forms.CharField(required=True, min_length=6)

