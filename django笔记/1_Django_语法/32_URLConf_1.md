#### Django如何处理一个请求

当一个用户通过网页发送一个请求给Django网站，Django执行过程如下：
1. 首先访问项目下的settings.py文件中 ROOT_URLCONF = 'test1.urls'
2. 执行项目包下的urls.py文件中的urlpatterns列表
3. 执行应用包下的urls.py文件中的urlpatterns列表
4. 根据匹配的url正则调用相应的视图函数/通用视图
5. 如果没有匹配的正则，将会自动调用Django错误处理页面

#### url函数配置方式
- 方式1
```
#student/urls.py

#coding=utf-8

from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^query$',views.queryAll)

]

#student/views.py

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def queryAll(request):

    return HttpResponse('hello world')
    
    
    

#访问地址
http://127.0.0.1:8000/student/query


```
- 方式2:位置传参
```
#student/urls.py

#coding=utf-8

from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^query$',views.queryAll),
    url(r'^query/(\d{2})$',views.queryAll),

]


#student/views.py

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def queryAll(request,sno):
    print sno
    return HttpResponse('hello world')


#访问地址
http://127.0.0.1:8000/student/query/12

```


- 方式3：关键字传参
```
urlpatterns=[
    url(r'^query$',views.queryAll),
    url(r'^query/(\d{2})$',views.queryAll),
    url(r'^query/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', views.queryAll),

]


def queryAll(request,year,day,month):
    print year,month,day
    return HttpResponse('hello world')
    
    
#访问地址
http://127.0.0.1:8000/student/query/2008/10/12/   
 
 
```

- 方式4：加载其他映射文件
```
from django.conf.urls import include, url

urlpatterns = [
     
    url(r'^community/', include('aggregator.urls')),

]

```

- 方式5：传参(参数名必须保持一致)
```
urlpatterns=[
    url(r'^query$',views.queryAll),
    url(r'^query/(\d{2})$',views.queryAll),
    url(r'^query/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', views.queryAll),
    url(r'^query/(?P<num1>\d{3})/$',views.queryAll,{'hello':'123'}),
]



def queryAll(request,num1,hello):
    print num1,hello
    return HttpResponse('hello world')
    
#访问地址   
http://127.0.0.1:8000/student/query/888/
```













