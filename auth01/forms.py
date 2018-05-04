from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth.models import User


class CaptchaForm(forms.Form):
    capt = CaptchaField()


# class RegisterForm(forms.Form):
#     username = forms.CharField(label='用户名', error_messages={'required', '用户名不能为空'})
#     password = forms.CharField(label='密 码', error_messages={'required', '密码不能为空'})
#     emails = forms.EmailField(label='邮箱')
#     capt = CaptchaField()
    # 全局验证
    # 局部验证
    # def clean(self):


class RegisterForm(forms.ModelForm):
    capt = CaptchaField()

    class Meta:
        model = User
        fields = ['username', 'password', 'email']
