from django import forms


# 查看templates/index.html
class SearchForm(forms.Form):
    # 验证提交的明星姓名，包括包含内容，最小长度为2
    name = forms.CharField(required=True, min_length=2)
