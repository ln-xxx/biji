#### 配置URL

```
#coding=utf-8

from django.conf.urls import url
import views

urlpatterns=[
    url(r'^sessionlogin/$',views.sessionlogin_view),
    url(r'^usercenter/$',views.center_view),

]

```




#### 创建视图函数

```
class User(object):
    def __init__(self,uname,pwd):
        self.uname = uname
        self.pwd = pwd


import jsonpickle

def sessionlogin_view(request):
    uname = request.GET.get('uname','')
    pwd = request.GET.get('pwd','')

    if uname=='zhangsan' and pwd=='123':
        user = User(uname,pwd)

        request.session['user'] = jsonpickle.dumps(user)
        return HttpResponseRedirect('/student/usercenter/')

    return HttpResponse('登录失败')


def center_view(request):
    user = jsonpickle.loads(request.session['user'])

    return HttpResponse('欢迎%s登录成功！'%user.uname)

```





















