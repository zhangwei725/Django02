from django.shortcuts import render, redirect

from form01.froms import TestForm, UserModelForm


# def test(request):
#     # test_form = TestForm(inital={'choices': [(1, '女'), (2, '男')], 'username': 'xiaoming'})
#     test_form = TestForm()
#     # 表示通过所有的验证  True   False
#     # 如果返回False 表示数据不符合我们的业务规范,不应该去执行保存的操作
#     # has_changed 判断用户是否操作了 如果操作了 返回True,否则返回False
#     if test_form.is_valid() and test_form.has_changed():
#         # 获取用户传递的数据
#         # uname = test_form.cleaned_data['username']  # {'username' :'123456'}
#         # passwd = test_form.cleaned_data['password']  # {'username' :'123456'}
#         # 保存数据
#         # User.objects.create(username=uname)
#     return render(request, 'form01.html', {'form': test_from})
# 后台统一返回json  restful   flask
def register(request):
    if request.method == 'POST':
        user_form = UserModelForm(request.POST)
        if user_form.is_valid():
            user_form.save()
        return redirect('success.html')
    else:
        user_form = UserModelForm()
    return render(request, 'register.html', {'user_form': user_form})