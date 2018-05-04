import datetime
#  认证  + 验证
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin

# 这个是1.10以前的写法
# class Middle1(object):
#     # 请求到达view之前
#     def process_request(self, request):
#         print('middle1------>request')
#
#     def process_view(self, request, view_func, view_args, view_kwargs):
#         print('middle1------>view')
#         return HttpResponse('middle1 拦截了!!!!')
#
#     def process_exception(self, request, exception):
#         print('middle1------>exception')
#
#     def process_template_response(self, request, response):
#         print('middle1------>exception')
#         return response
#
#     def process_response(self, request, response):
#         print('middle1------>response')
#         return response
#
#
# class Middle2(object):
#     # 请求到达view之前
#     def process_request(self, request):
#         print('middle2------>request')
#
#     def process_view(self, request, view_func, view_args, view_kwargs):
#         print('middle2------>view')
#
#     #     view返回Response之后
#
#     def process_exception(self, request, exception):
#         print('middle2------>exception')
#
#     def process_template_response(self, request, response):
#         print('middle2------>exception')
#         return response
#
#     def process_response(self, request, response):
#         print('middle2------>response')
#         return response

# 1.10以上的版本  兼容1.9版本

# 同一ip地址十分钟禁止重复注册
# 1.获取客服端的ｉｐ地址  记录时间  可以记录ｓｅｓｓｉｏｎ　　　ｄｂ　　ｆｉｌｅ
# ２.通过查询ｉｐ地址最后一次时间　跟当前的这个时间进行比较　＜　６００禁止注册
from middleware01.models import Ip


class M01(MiddlewareMixin):

    #
    def process_view(self, request, view_func, view_args, view_kwargs):
        # 获取客服端的ip地址
        if request.get_path() == '/account/register/':
            addr = request.Meta['REMOTE_ADDR']
            client_ip = Ip.objects.get(cip=addr)
            if client_ip:
                if (datetime.datetime.now() - client_ip.last_time).total_seconds() < 10 * 60:
                    return HttpResponse('十分钟之内禁止注册')
                client_ip.last_time = datetime.datetime.now()
                client_ip.save()

    def process_exception(self, request, exception):
        print('M01------>exception')

    def process_template_response(self, request, response):
        print('M01------>exception')
        return response


class M02(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        print('M02------>view')

    def process_exception(self, request, exception):
        print('M02------>exception')

    def process_template_response(self, request, response):
        print('M02------>exception')
        return response

    def process_response(self, request, response):
        print('m02------>response')
        return response
