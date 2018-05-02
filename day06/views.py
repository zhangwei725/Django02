from datetime import datetime

from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import View

from Django02 import settings
from day06.models import UserInfo


def index(request):
    return render(request, 'index.html')


class UploadFile(View):
    """"

    前端 表单 必须是post请求 ENCTYPE=multipart/form-data
    input  type=‘file’
    如果发现request.FILES如果是空 检查是是否是post请求
    """

    def post(self, request):
        # request.FILES 是一个字典  包含
        #     文件名称
        #     文件的内容
        #     uploadfile
        upload_file = request.FILES.get('img')
        '''
           # read()
           读取文件上传的数据,慎用
            multiple_chunks(size)
            判断文件是否足够大 
            chunks(size)  
            返回一个生成起对象，把上传的文件切割 可以制定size 
            name
            获取文件的名称
            size 获取文件的大小
            content_type  上传文件的类型
            charset   文件的编码  
           
        '''
        # 123.jpg  xx.pdf
        """
        客服上传文件  
        服务器段保存文件 二进制的数据 
        保存文件的路径到数据
        """
        """
        对客服端上传文件服务器要重命名，防止同名文件覆盖
        对路径进行细分 对文件进行重命名（保证名字是唯一的）
        1.获取文件的后缀名  os.path.splittext()  
        str.split()
        
        """
        # xxx.jpg xxx.pdf     IMG_20180221124536.jpg
        # [‘文件名称’ ‘后缀名’]
        file_name_last = upload_file.name[upload_file.name.rfind('.'):]
        file_name = 'IMG_{}{}'.format(datetime.now().strftime('%Y%m%d%H%M%S'), file_name_last)
        with open(settings.MEDIA_ROOT + '/img/' + file_name, 'wb') as file:
            # 把二进制的数据保存到服务器
            for chunk in upload_file.chunks():
                file.write(chunk)
        return render(request, 'success.html')


def upload(request):
    if request.method == 'POST':
        for value in request.FILES.get('head'):
            print(value)
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = UserInfo()
        user.head = request.FILES.get('head')
        user.username = username
        user.password = password
        user.save()
    return render(request, 'index.html')
