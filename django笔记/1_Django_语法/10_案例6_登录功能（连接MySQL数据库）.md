#### 安装MySQL-python==1.2.5库
```
#方式1：
    运行窗口：
    pip install wheel
    pip install MySQL_python-1.2.5-cp27-none-win_amd64.whl
    
#方式2：
    pycharm/settings/project interpreter中添加库
    
#方式3：
    pip2.7 install MySQL-python==1.2.5

```


#### 修改settings.py文件
```
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',#数据库连接器
            'NAME': 'logindemo',#数据库名称
            'HOST':'127.0.0.1',#数据库主机地址
            'PORT':'3306',#数据库端口
            'USER':'root',#数据库用户名
            'PASSWORD':'123456'#数据库密码
        }
    }


```

#### 配置模型类(student/models.py)

```
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Stu(models.Model):
    sname = models.CharField(max_length=20,unique=True)
    spwd = models.CharField(max_length=20,unique=True)

    def __unicode__(self):
        return u'Stu:%s,%s'%(self.sname,self.spwd)



```


#### 生成数据库表
```

   
#创建当前应用的迁移文件
python manage.py makemigrations student

#生成数据库表
python manage.py migrate



```

#### 配置URL

```
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^student/', include('student.urls')),
]

```

```
#coding=utf-8

from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$',views.login_view),
    url(r'^login/',views.to_login_view)
]

```



#### 配置函数视图

```

#处理登录功能
def doLogin_view(request):
    #接收请求参数
    uname = request.POST.get('uname','')
    pwd = request.POST.get('pwd','')

    #判断是否登录成功
    count = Stu.objects.filter(sname=uname,spwd=pwd).count()
    

    if count==1:
        return HttpResponse('登录成功！')
    else:
        return HttpResponse('登录失败！')

```




































