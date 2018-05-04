import json

from captcha.helpers import captcha_image_url
from captcha.models import CaptchaStore
from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import render

# 实现用户系统的需要的
# 1  导入auth模块
# 2  导入验证码  captcha  pillow

# django-simple-captcha  验证
from auth01.forms import CaptchaForm, RegisterForm


def yanzhen(request):
    if request.method == "POST":
        capt = CaptchaForm(request.POST)
        if capt.is_valid():
            # 验证通过
            pass
    else:
        capt = CaptchaForm()
    return render(request, 'test_capt.html', {'capt': capt})


def register(request):
    if request.method == "POST":
        capt = RegisterForm(request.POST)
        if capt.is_valid():
            capt.save()
            # 认证用户
            # auth.authenticate(request, user)
    else:
        capt = RegisterForm()
    return render(request, 'account/register.html', {'capt': capt})
#  后台
#  前端  小程序  react
#  ios  android
# 生成验证码  返回到前端
def get_verify_code(request):
    verify_code = {}
    key = CaptchaStore.generate_key()
    verify_code.update(haskey=key)
    verify_code.update(img_url=captcha_image_url(key=key))
    # json数据 本质是一个字符串
    # json.loads()解析
    return HttpResponse(json.dumps(verify_code), content_type='Application/json')
