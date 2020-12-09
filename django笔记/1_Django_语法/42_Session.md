1. cookie引入session：

    cookie看似解决了HTTP（短连接、无状态）的会话保持问题，但把全部用户数据保存在客户端，存在安全隐患。

2. cookie+session 
    把关于用户的数据保存在服务端，在客户端cookie里加一个sessionID(随机字符串)
    基于以上原因：cook+session组合就此作古了单单使用cookie做会话保持的方式；

3. cookie+session的工作流程：

    (1)、当用户来访问服务端时,服务端生成一个随机字符串；

    (2)、当用户登录成功后 把 {sessionID :随机字符串} 组织成键值对 加到 cookie里发送给用户；

    (3)、服务器以发送给客户端 cookie中的随机字符串做键，用户信息做值，保存用户信息；




4. 保存在服务端session数据格式
    session_key    SessionStore()  

        {
        
         session_key                                       数据字典
        
        sessionid1：                     {id：1,nam："alex"，account：1000000000 }，
        
        sessionid2：                     {id：1,nam："eric"，account：10}
        
        }






#### Session中存储值

```
def session_view(request):
    # SessionStore()
    #设置session数据
    # request.session['user']='zhangsan'

    #设置过期时间（单位秒）
    # request.session.set_expiry(10*60)

    #删除当前user对应的session数据
    # del request.session['user']

    #删除所有session数据（不清空数据库，只删除cookie中的sessionid）
    # request.session.clear()

    #清空数据库中的session数据
    # request.session.flush()

    #获取sessionid
    # print request.session.session_key

    return HttpResponse('保存成功！')

```


#### Session中取值

```
def getsession_view(request):

    #session中取值
    user = request.session['user']
    # user = request.session.get('user')

    return HttpResponse('datas:%s'%user)


```


#### Session存储引擎


```
#settings.py文件中
    #Session默认存储在数据库
	SESSION_ENGINE = 'django.contrib.sessions.backends.db'

    #内存

	SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
	# 可以存储自定义对象，内存不用json序列化
	# 服务器重启，数据丢失
 
    #内存+数据库（双缓存）

	SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'	
	# 内存速度快，数据库慢
	# 储存的步骤，先存到内存，在存到数据库
	# 先从内存读，再从数据库读，如果从数据库读到了，再放入内存

    #file
 	
 	SESSION_ENGINE = 'django.contrib.sessions.backends.file'
	SESSION_FILE_PATH = os.getcwd()
    
    #signed_cookies

	SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'
	# 将数据加密，存到cookie中了（存到浏览器）

```












