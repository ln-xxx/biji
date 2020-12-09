#### GET请求报文

```
    GET http://127.0.0.1:8000/student/login/?uname=zhangsan&pwd=123 HTTP/1.1
    Host: 127.0.0.1:8000
    Connection: keep-alive
    Cache-Control: max-age=0
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
    Accept-Encoding: gzip, deflate, br
    Accept-Language: zh-CN,zh;q=0.9
    
    
```


#### GET响应报文

```
    HTTP/1.0 200 OK
    Date: Sun, 01 Apr 2018 12:46:21 GMT
    Server: WSGIServer/0.1 Python/2.7.13
    X-Frame-Options: SAMEORIGIN
    Content-Type: text/html; charset=utf-8
    Content-Length: 15
    
    登录成功！

```



#### POST请求报文

```
    POST http://127.0.0.1:8000/student/login/ HTTP/1.1
    Host: 127.0.0.1:8000
    Connection: keep-alive
    Content-Length: 22
    Cache-Control: max-age=0
    Origin: http://127.0.0.1:8000
    Upgrade-Insecure-Requests: 1
    Content-Type: application/x-www-form-urlencoded
    User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
    Referer: http://127.0.0.1:8000/student/
    Accept-Encoding: gzip, deflate, br
    Accept-Language: zh-CN,zh;q=0.9
    Cookie: csrftoken=Vybx47cUL2j3O8aui6ma5OOlXKhWRsMf2VEd7QHuzuhn6oizRlh41LiZGCMmN0hS
    
    uname=zhangsan&pwd=123
    
```


#### POST响应报文

```

    HTTP/1.0 200 OK
    Date: Sun, 01 Apr 2018 13:14:07 GMT
    Server: WSGIServer/0.1 Python/2.7.13
    X-Frame-Options: SAMEORIGIN
    Content-Type: text/html; charset=utf-8
    Content-Length: 15
    
    登录成功！

```

#### GET和POST请求区别

	1. POST请求的请求参数在请求实体内容中，GET请求的请求参数存放在URL中。
	2. POST请求比GET请求安全？（都不安全）
	3. GET请求的URL参数长度有限（不超过2K），POST没有长度限制
	4. GET请求一般做查询（有缓存），POST请求一般做添加/删除/修改（无缓存）
	5. Django服务器GET/POST请求为什么接受参数方式都一样？
		因为他们都是QueryDict对象（django.http.request）


#### GET请求方式
    1. <form method="get">
    2. 浏览器地址栏直接访问
    3. <a href="/student/">超链接</a>
    4. window.location.href="/student/"
    
    
#### POST请求方式
    1. <form method="post">
    

#### HTTP特性
    1. HTTP1.1版本后支持长连接
    2. 单向性协议（必须先有请求后有响应）
    3. 无状态的协议
        Cookie:客户端相关
        Session：服务器相关
  