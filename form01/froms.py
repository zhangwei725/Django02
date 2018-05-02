# 专门用来存放 from对象
"""
1. 第一步先定义对象

"""
from django import forms


class TestForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=15, min_length=6,
                               error_messages={'max_length': u'最大为15位', 'min_length': '最小是6位'})
    is_accept = forms.BooleanField(label='同意', error_messages={'required': '必须接受'})
    file = forms.FileField(label='请选择上传的文件', required=False)
    img = forms.ImageField(label='请选择图片', required=False)
    # datetime.date
    test_date = forms.DateField(label='请输入日期', input_formats=['%Y-%m-%d'])
    test_datetime = forms.DateTimeField(label='请输入日期', input_formats=['%Y-%m-%d %H%M%S'])
    sex = forms.ChoiceField(label='性别', choices=[(1, '女'), (2, '男')])

