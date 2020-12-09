#### 客户端保存数据

#### 设置cookie
1. 普通

response.set_cookie("uname","zhangsan",expires=value,path='/' )

2. 加盐

普通cookie是明文传输的，可以直接在客户端直接打开，所以需要加盐，解盐之后才能查看

response.set_signed_cookie('k','v',salt="fdsa")
 
#### 获取cookie
1. 普通
```
request.COOKIES['hello']
request.COOKIES.get('hello','')
```
2. 加盐
```
request.get_signed_cookie('k',salt='fdsa')

```

#### 删除值

```
#设置过期
1. 默认情况关闭浏览器就失效
2. max_age=-1(单位秒)
3. expires=datetime.datetime.today()+datetime.timedelta(days=-2)（单位日期类型）
4. response.delete_cookie('login',path='/student/login/')

```


#### 涉及属性
```
1、max_age=1 ：cookie生效的时间，单位是秒

2、expires:具体过期日期  

3、path='/'：指定那个url可以访问到cookie；'/'是所有 path='/'

4、domain=None（None代表当前域名）：指定那个域名以及它下面的二级域名（子域名）可以访问这个cookie
   domain='.baidu.com'



```


#### 语法
```
#设置cookie
def index_view(request):
    import datetime
    
    response = HttpResponse()
    # response.set_cookie('hello','123',max_age=24*60*60*3,path='/student/abc/')
    
    # response.set_cookie('hello','123',path='/student/abc/',expires=datetime.datetime.today()+datetime.timedelta(days=4))

    response.set_signed_cookie('hello','123',salt='hahaha',path='/student/abc/',expires=datetime.datetime.today()+datetime.timedelta(days=4))

    return response

```

```
#获取cookie
def abc_view(request):
    #返回所有cookie数据
    print request.COOKIES
    #返回KEY='hello'的数据
    print request.get_signed_cookie('hello',salt='hahaha')
    
    return HttpResponse('hello')

```





















