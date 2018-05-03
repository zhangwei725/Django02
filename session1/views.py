from django.shortcuts import render


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
