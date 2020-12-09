#### 逆向解析(防止硬编码)
```
#student/urls.py

from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^query$',views.queryAll),
    url(r'^query/(\d{2})$',views.queryAll),
    url(r'^query/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2})/$', views.queryAll),
    url(r'^query/(?P<num1>\d{3})/$',views.queryAll,{'hello':'123'}),
    url(r'^query1/([0-9]{4})/$', views.queryAll, name='hello'),
    url(r'^$', views.index_view),
]

#student/views.py

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def queryAll(request,num1):
    print num1
    return HttpResponse('hello world')

#通过模板页面逆向访问
def index_view(request):
    return render(request,'index.html')

#通过Python代码逆向访问
def index_view(request):
    # return render(request,'index.html')
    return HttpResponseRedirect(reverse('hello',args=(2018,)))
    
    
    

#templates/index.html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <a href="{% url 'hello' 2008 %}">访问</a>

</body>
</html>




```
- 方式2
```

#项目包/urls.py

from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^student/', include('student.urls',namespace='stu',app_name='student')),
]

#应用包/urls.py

#coding=utf-8

from django.conf.urls import url
from . import views

urlpatterns=[

    url(r'^$', views.Index.as_view()),
    url(r'^query2/',views.Login.as_view(),name='login')
]


#应用包/views.py

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

 


from django.views import View
class Index(View):
    def get(self,request):
        return render(request,'index.html')


class Login(View):
    def get(self,request):
        return HttpResponse('hello')


#templates/index.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <a href="{% url 'stu:login' %}">访问</a>

</body>
</html>


```

































