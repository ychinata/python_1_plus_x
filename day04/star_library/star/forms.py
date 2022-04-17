from django import forms


class SearchForm(forms.Form):
    # 验证提交的明星姓名，必须包含内容，最小长度是2
    name = forms.CharField(required=True, min_length=2)
