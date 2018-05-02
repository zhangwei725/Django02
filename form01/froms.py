# 专门用来存放 from对象
"""
1. 第一步先定义对象

"""
from django import forms
from django.core.exceptions import ValidationError

from form01 import models

"""
field 属性

label 
required 
error_message
widget

如果修改默认的widget
给widget添加一下额外的属性


常用的api

forms.fields


"""


class TestForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=15, min_length=6,
                               widget=(forms.TextInput(attrs={'placeholder': '请输入用户名'})),
                               error_messages={'max_length': u'最大为15位', 'min_length': '最小是6位'})
    password = forms.CharField(label='密码', widget=(forms.PasswordInput(attrs={'placeholder': '请输入密码'})))

    is_accept = forms.BooleanField(label='同意', error_messages={'required': '必须接受'})
    file = forms.FileField(label='请选择上传的文件', required=False)
    img = forms.ImageField(label='请选择图片', required=False)
    # datetime.date
    test_date = forms.DateField(label='请输入日期', input_formats=['%Y-%m-%d'])
    test_datetime = forms.DateTimeField(label='请输入日期', input_formats=['%Y-%m-%d %H%M%S'])
    sex = forms.ChoiceField(label='性别', choices='choices')
    email = forms.EmailField(label='邮箱', max_length=20)

    def __init__(self):
        super().__init__()
        # = {'': [[(1, '女'), (2, '男')]]}

    # 重写验证
    #  全局   局部
    def clean_username(self):
        # 表示用户名必须包含字母
        if self.cleaned_data['username'].isalnum():
            return self.cleaned_data['username']
        else:
            raise ValidationError('用户名必须包含字母')


class UserModelForm(forms.ModelForm):
    class Meta:
        model = models.User
        # 所有的属性都生成form
        # fields = '__all__'
        # 指定特定的属性生产form
        # fields = ['username', 'password']
        # 不包含
        exclude = ['is_del']
