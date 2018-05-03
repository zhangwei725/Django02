from django.http import HttpResponse
from django.shortcuts import render, redirect

from session1.models import User


def test_cookie(request):
    resp = render(request, 'index.html')
    username = request.COOKIES.get('username')
    if not username:
        resp.set_cookie('username', 'zhangsan')
    return resp


def test_cookie2(request):
    resp = render(request, 'index.html')
    username = request.get_signed_cookie('username', default='', salt='test')
    if not username:
        # path/ 限制访问的路径
        # /session1/test2/ 表示  http://ip:端口/session1/test2/ 或者/xxx 的能获取这个cooki信息
        # 其他的比如说像http://ip:端口/session1/test1/ 或者 http://ip:端口/session1/test1都获取不到这个cookie信息
        resp.set_signed_cookie('username', 'xiaohong', salt='test',
                               max_age=7 * 24 * 60 * 60,
                               path='/session1/test2/', )
        # 删除cookie
        # resp.delete_cookie('username')
    return resp


# 不要存中文

# 缺点 安全不高  而且客服端可以禁用

# 数据存在客服端  减轻服务器的压力

'''
在settings.py中要开启,默认已经开启 如果你用会话追踪技术可以去关闭
django 处理session数据的方式
1. 存在数据库中(默认)
2. 缓存
3. 文件中
4. 缓存+ 数据库
5. 加密cookie
6.  django-redis-session(第三方 需要单独安装) 
'''


# {'username': 'xiaoming'}
def test_session(request):
    # request.session['username'] # key不存在就报错
    username = request.session.get('username', default=None)
    # request.sesion['user'] = '12313'
    # 设置值 如果存在就修改,不存在就设置
    request.session.setdefault('username', '123132')
    # 获取所有的key
    # request.session.keys()
    # 获取的所有的值
    # request.session.values()
    # 获取所有键值对
    request.session.iteritems()
    # 设置session的过期时间
    request.sesion.set_expiry(2 * 24 * 60 * 60)

    """
    如果设置的值是个整数  多少秒之后失效
    如果是一个datetime对象 在制定的日期失效
    如果是0 表示浏览器关闭失效
    如果是None  表示参照全局的设置
    """
    pass


def test_session2(request):
    count = request.session.get('count', default=0)
    if count == 0:
        count = 1
        request.session.setdefault('count', count)
    else:
        count += 1
        request.session['count'] = count
    # 不存在就设置,存在就不设置
    return HttpResponse('次数---->{}'.format(count))

# session实现免登录


def login(request):
    username = request.GET.get('username')
    password = request.GET.get('password')
    user = User.objects.filter(username=username, password=password).first()
    if user:
        request.session.setdefault('username', user.username)
        request.session.setdefault('username', user.id)
        request.session.set_expiry(7 * 24 * 60 * 60)
        return redirect('/session1/home', {'username': username})
    else:
        render(request, '/login.html', {'msg': '账号密码错误', })

def home(request):
    username = request.session.get('username')
    return render(request, 'index1.html', {'username': username})
