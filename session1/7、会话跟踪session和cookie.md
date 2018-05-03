## 会话跟踪

## 一、什么是会话跟踪

> 1、cookie不属于http协议范围，由于http协议无法保持状态，但实际情况，我们却又需要“保持状态”，因此cookie就是在这样一个场景下诞生。
>
> cookie的工作原理是：由服务器产生内容，浏览器收到请求后保存在本地；当浏览器再次访问时，浏览器会自动带上cookie，这样服务器就能通过cookie的内容来判断这个是“谁”了。
>
> 2、cookie虽然在一定程度上解决了“保持状态”的需求，但是由于cookie本身最大支持4096字节，以及cookie本身保存在客户端，可能被拦截或窃取，因此就需要有一种新的东西，它能支持更多的字节，并且他保存在服务器，有较高的安全性。这就是session。
>
> 问题来了，基于http协议的无状态特征，服务器根本就不知道访问者是“谁”。那么上述的cookie就起到桥接的作用。
>
> 我们可以给每个客户端的cookie分配一个唯一的id，这样用户在访问时，通过cookie，服务器就知道来的人是“谁”。然后我们再根据不同的cookie的id，在服务器上保存一段时间的私密资料，如“账号密码”等等。
>
> 3、总结而言：cookie弥补了http无状态的不足，让服务器知道来的人是“谁”；但是cookie以文本的形式保存在本地，自身安全性较差；所以我们就通过cookie识别不同的用户，对应的在session里保存私密的信息以及超过4096字节的文本。
>
> 4、另外，上述所说的cookie和session其实是共通性的东西，不限于语言和框架
>
> Cookie通过在客户端记录信息确定用户身份，Session通过在服务器端记录信息确定用户身份
>
> 1. Session技术：会话数据保存在服务器端
> 2. Cookie技术: 会话数据保存在浏览器客户端。

## 二、Session

### 1、概要

> session 机制是⼀一种服务器端的机制
>
> 当程序需要为某个客户端的请求创建⼀一个 session 的时候， 服务器首先检查 这个客户端的请求⾥是否已包含了⼀个 session 标识 - 称为 session id ，如果 已包含一个 session id 则说明以前已经为此客户端创建过 session ，服务器就 按照 session id 把这个 session 检索出来使⽤用（如果检索不到，可能会新建一 个），如果客户端请求不包含 session id ，则为此客户端创建一个 session 并 且⽣成一个与此 session 相关联的 session id ，session id 的值应该是⼀个既 不会重复，又不容易被找到规律以仿造的字符串，这个 session id 将被在本次 响应中返回给客户端保存.

### 2、Django 的session

1. 说明

   Django中默认支持Session，其内部提供了5种类型的Session供开发者使用：

   也可以使用第三方的django-redis-sessions

2. 处理方式

   - 数据库（默认）
   - 缓存
   - 文件
   - 缓存+数据库
   - 加密cookie
   - django-redis-sessions(第三方)

3. 配置

   1、如果是数据库，需要在settings.py中配置如下：

   ```
   SESSION_ENGINE = 'django.contrib.sessions.backends.db' （引擎（默认））
   ```

   2、如果是缓存session,需要在settings.py中配置如下：

   ```
   SESSION_ENGINE = 'django.contrib.sessions.backends.cache'（引擎）
   SESSION_CACHE_ALIAS= 'default'  使用的缓存别名（默认内存缓存，也可以是memcache），此处别名依赖缓存的设置
   ```

   3、如果是文件session, 需要在settings.py中配置如下：

   ```
   SESSION_ENGINE = 'django.contrib.sessions.backends.file' (引擎)
   SESSION_FILE_PATH=None  缓存文件路径，如果为None，则使用tempfile模块获取一个临时地址tempfile.gettempdir()   
   如：/var/folders/d4/j9tj0gz93dg06bmwxmhh6_xm0000gn/T
   ```

   4、如果是缓存+数据库session，需要在settings.py中配置如下：

   ```
   SESSION_ENGINE='django.contrib.sessions.backends.cached_db' （引擎）
   ```


### 3、Django使用

#### 1、前期准备工作

1. 在setting.py中配置(默认已经加入)

   ```
   MIDDLEWARE = [
       # 会话支持中间件
       'django.contrib.sessions.middleware.SessionMiddleware',
   ]

   INSTALLED_APPS = [
       'django.contrib.sessions',
   ]
   ```

2. session配置文件

   ```python
   SESSION_COOKIE_NAME="sessionid"  # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串
   SESSION_COOKIE_PATH="/"  # Session的cookie保存的路径
   SESSION_COOKIE_DOMAIN = None  # Session的cookie保存的域名
   SESSION_COOKIE_SECURE = False  # 是否Https传输cookie
   SESSION_COOKIE_HTTPONLY = True  # 是否Session的cookie只支持http传输
   SESSION_COOKIE_AGE = 7*24*60*60  # Session的cookie失效日期（2周） 默认1209600秒
   SESSION_EXPIRE_AT_BROWSER_CLOSE =True  # 是否关闭浏览器使得Session过期

   SESSION_SAVE_EVERY_REQUEST = True  
   #如果你设置了session的过期时间 30分钟后，这个参数是False30分钟过后，session准时失效
   #如果设置 True，在30分钟期间有请求服务端，就不会过期！
   ```

   ​

#### 2、常用参数

1. 设置

   ```
   request.session['key'] = 123
   request.session.setdefault('key','default') # 存在则不设置
   ```

2. 获取

   ```
   request.session['key'] #如果不存在则会报错
   request.session.get('key',None) #这样取值的不报错，没有拿None
   ```

3. 删除

   ```
    del request.session['key']
   ```

4. 获取所有的键

   ```
      request.session.keys()
   ```

5. 获取所有的值

   ```
    request.session.values()
    request.session.itervalues()
   ```

6. 获取所有的键值对

   ```
   request.session.iteritems()
   ```

7. session的随机字符串

   ```python
   request.session.session_key   
   ```

8. 清除所有的过期session

   ```python
   request.session.clear_expired()
   #sessionID在客户端，过期后自动失效；但session信息存储在数据库里，sessionID过期后怎么删除呢？无法动态删过期的session，可执行这个方法！（数据库中不仅存储了session 还有该session的过期时间，这个方法就是where数据库里时间过期的session删除掉）
   ```

9. 检测随机字符串是否存在

   ```
   request.session.exists("session_key")
   ```

10. 删除当前用户所有的session数据

  ```
  request.session.delete("session_key") 
  ```

11. 设置session过期时间

    ```python
    request.session.set_expiry(value) 
    '''
    1. 如果value是个整数，session会在些秒数后失效。
    2. 如果value是个datatime或timedelta，session就会在这个时间后失效。 
    3. 如果value是0,用户关闭浏览器session就会失效。
    4. 如果value是None,session会依赖全局session失效策略。
    '''
    ```

12. 从session中删除数据,然后再生数据,比如django的logout()函数就会调用它.

    ```
    request.session.flush()
    ```

13. 设置一个test cookie来判断用户浏览器是否接受cookie.

    ```
    request.session.set_test_cookie()
    ```

14. 当设置了test cookie后返回True或Flase判断用户浏览器是否接受cookie.所以要先执行 

    ```
    request.session.test_cookie_worked()
    ```

15. 删除test cookie,测试完成后删除

    ```
    request.session.delete_test_cookie()
    ```
    ```
    if request.method == 'POST':
        if request.session.test_cookie_worked():	
          request.session.delete_test_cookie()	 
          return HttpResponse("You're logged in.")
        else:
          return HttpResponse("Please enable cookies and try again.")
    request.session.set_test_cookie()	
    ```

#### 举个栗子

1. 登录

   ```python
   def login(request):
       if request.method=='GET':
           return render(request,'login.html')
       else:
           name=request.POST.get('username')
           pwd=request.POST.get('password')
           user = models.User.objects.filter(username=name, passwprd=pwd).first()
           if obj:
               #1、生成随机字符串（sessionID）
               #2、通过cookie发送给客户端
               #3、服务端保存
               request.session['name']=user.username #在Django 中一句话搞定
               return redirect('/index')
           else:
               return render(request,'login.html',{'msg':"用户名/密码错误"})

   def index(request):
       #1、获取客户端的 sessionID
       #2、在服务端查找是否存在 这个sessionID
       #3、在服务端查看对应的key sessionID键的值中是否有name（有值就是登录过了！！）
       name=request.session.get('name')
       if name:
           return render(request,'index.html',{'msg':name})
       else:return redirect('/login/')
   ```

2. 必须登录才能访问界面

   ```
   from django.shortcuts import render
   from django.shortcuts import redirect
   def login(request):
       if request.method=="POST":
           username=request.POST['username']
           pwd=request.POST['passwd']
           if username=='abc' and pwd=='123':
               #设置session内部的字典内容
               request.session['is_login']='true'
               request.session['username']='abc'
               #登录成功就将url重定向到后台的url
               return redirect('/backend/')
       #登录不成功或第一访问就停留在登录页面
       return render(request,'login.html')
   def backend(request):
       """
       这里必须用读取字典的get()方法把is_login的value缺省设置为False，
       当用户访问backend这个url先尝试获取这个浏览器对应的session中的
       is_login的值。如果对方登录成功的话，在login里就已经把is_login
       的值修改为了True,反之这个值就是False的
       """
       is_login=request.session.get('is_login',False)
       #如果为真，就说明用户是正常登陆的
       if is_login:
           #获取字典的内容并传入页面文件
           cookie_content=request.COOKIES
           session_content=request.session
           username=request.session['username']
           return render(request,'backend.html',
                         {
               'cookie_content':cookie_content,
               'session_content':session_content,
               'username':username
                         })
       else:
           """
           如果访问的时候没有携带正确的session，
           就直接被重定向url回login页面
           """
           return redirect('/login/')
   def logout(request):
       """
       直接通过request.session['is_login']回去返回的时候，
       如果is_login对应的value值不存在会导致程序异常。所以
       需要做异常处理
       """
   	request.session.pop('is_login')
       #点击注销之后，直接重定向回登录页面
       return redirect('/login/')

   ```

   ​

## 三、cookie

> ![](http://opzv089nq.bkt.clouddn.com/17-9-2/16370237.jpg)

### 1、概要

> 一种会话数据管理技术，该技术把会话数据保存在浏览器客户端
>
> Cookie具有不可跨域名性
>
> Cookies 是一中由服务器发送给客户的片段信息，存储在客户端浏览器的内容中或硬盘上在客户随后对该服务器的请求中发回它，Cookies以键值对的形式记录会话跟踪的内容，服务器利用响应报头 Set-Cookie来发送Cookie信息，由于涉及隐私权和安全性方面的问题，用户在使用浏览器时，可以选择禁用Cookie，web服务器就无法利用Cookie跟踪用户的会话了，要解决这个问题需要重写URL服务器可以根据Cookie来跟踪客户状态，这对于需要区别客户的场合（如电子商务,推荐等功能）特别有用

### 2、cookie的构成

> Cookie 的内容主要包括
>
> 1. 名字
> 2. 值
> 3. 过期时间
> 4. 路径和域
>    1. 域和路径的主要作用限制cookie的使用范围
>    2. 域指的 baidu.com
>    3. 路径就是跟在域名后面的 URL 路径，比如 /app/login 等等

### 3、工作流程

1. 首先浏览器向服务器发出请求。
2. 服务器就会根据需要生成一个Cookie对象，并且把数据保存在该对象内。
3. 然后把该Cookie对象放在响应头，一并发送回浏览器。
4. 浏览器接收服务器响应后，该Cookie保存在浏览器端。
5. 当下一次浏览器再次访问那个服务器，就会把这个Cookie放在请求头内一并发给服务器
6. 服务器从请求头提取出该Cookie，判别里面的数据，然后作出相应的动作。

### 4、常用参数

1. key

   键

2. value

   值

3. max_age=1

   cookie生效的时间，单位是秒

4. expires

   具体过期日期

5. path='/'

   指定那个url可以访问到cookie；‘/’是所有； path='/'**

6. domain=None（None代表当前域名）

   指定那个域名以及它下面的二级域名（子域名）可以访问这个cookie**

7. secure=False

   https安全相关

8. httponly

   值应用于http传输，JavaScript无法获取

### 5、django操作cookie

#### 1、获取Cookie

1. 方式一

   ```
   request.COOKIES['key']
   ```

2. 方式二

   ```
   request.get_signed_cookie(key, default=RAISE_ERROR, salt='', max_age=None)
   #参数说明
   default: 默认值
   salt:    加密盐 内容可随便定义,解密时候要一样
   max_age: 后台控制过期时间
   ```

#### 2、设置Cookie

1. 获取HttpResponse对象

   ```
   rep = HttpResponse(...) 
   rep ＝ render(request, ...) 
   rep ＝ redirect()
   ```

2. 方式一

   ```
   rep.set_cookie(key,value,...)
   ```

3. 方式二

   ```
   rep.set_signed_cookie(key,value,salt='加密盐',...)
   ```

4. 示例代码

   ```
   def set_cookie(self, key,                 键
   　　　　　　　　　　　　 value='',            值
   　　　　　　　　　　　　 max_age=None,        超长时间
   　　　　　　　　　　　　 expires=None,        过期时间时间
   　　　　　　　　　　　　 path='/',           Cookie生效的路径，
                                            浏览器只会把cookie回传给带有该路径的页面，这样可以避免将cookie传给站点中的其他的应用。
                                            / 表示根路径，特殊的：根路径的cookie可以被任何url的页面访问
   　　　　　　　　　　　　 
                    domain=None,         
                        Cookie生效的域名,你可用这个参数来构造一个跨站cookie。
                        如， domain=".baidu.com"
                        所构造的cookie对下面这些站点都是可读的：
                        www.baidu.com 、 www.news.baidu.com
                        如果该参数设置为 None ，cookie只能由设置它的站点读取。
   　　　　　　　　　　secure=False,        
   　　　　　　　　　　	  如果设置为 True ，浏览器将通过HTTPS来回传cookie。
   　　　　　　　　　　httponly=False       
   　　　　　　　　　　    只能http协议传输，无法被JavaScript获取（不是绝对，底层抓包可以获取到也可以被覆盖）                                        
   ): 
   ```

#### 3、jQuery 操作

1. js代码

   ```python
   <script src='/static/js/jquery.cookie.js'></script>
   <script>
   $(function(){
        $.cookie("key", value,{ path: '/' });
   })
   </script>
   ```

#### 4、删除cookie

1. 方式

   ```
   rep.delete_cookie("cookie_key",path="/",domain=name)
   ```

2. 举个例子

   ```python
   rep.delete_cookie("username",path="/",domain=name)
   ```


综合小案例

1. 设置加密的cookie

   ```python
   def test_cookie1(request):
       username = request.get_signed_cookie('username', default='', salt='test')
       rep = render(request, 'index.html')
       if username:
           print(username)
       else:
           rep.set_signed_cookie('username', 'xm', salt='test', max_age=7 * 24 * 60 * 60, path='/')
       return rep
   ```






### 6、优点

1. 优点： 数据存在在客户端，减轻服务器端的压力，提高网站的性能。

2. 缺点：安全性不高：在客户端机很容易被查看或破解用户会话信息,容易被用户禁用    

## 四、其它

#### 1、Cookie和Session的区别：

1. **Cookie中只能保存ASCII字符串，Session中可以保存任意类型的数据**
2. **隐私策略不同**。Cookie存储在客户端，对客户端是可见的，可被客户端窥探、复制、修改。而Session存储在服务器上，不存在敏感信息泄露的风险
3. **有效期不同**。Cookie的过期时间可以被设置很长。Session依赖于名为SESSIONI的Cookie，其过期时间默认为-1，只要关闭了浏览器窗口，该Session就会过期，因此Session不能完成信息永久有效。如果Session的超时时间过长，服务器累计的Session就会越多，越容易导致内存溢出。
4. **服务器压力不同**。每个用户都会产生一个session，如果并发访问的用户过多，就会产生非常多的session，耗费大量的内存。因此，诸如Google、Baidu这样的网站，不太可能运用Session来追踪客户会话。
5. **浏览器支持不同**。Cookie运行在浏览器端，若浏览器不支持Cookie，需要运用Session和URL地址重写。
6. **跨域支持不同**。Cookie支持跨域访问（设置domain属性实现跨子域），Session不支持跨域访问