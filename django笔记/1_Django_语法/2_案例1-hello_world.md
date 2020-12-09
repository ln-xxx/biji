#### 创建Django项目 ####
        1. 创建方式：
         
         #方式1：终端输入
             django-admin startproject testmvt
             
         #方式2:
            pycharm中新建django项目
         


#### 配置URL ####
    ```
    from django.conf.urls import url
    from django.contrib import admin
    import views
    
    urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'^$', views.login_view),
    ]

    ```
    
#### 创建views.py文件 ####
```
#coding=utf-8
from django.http.response import HttpResponse


def login_view(request):
    return HttpResponse('hello world')
```

#### 启动服务器 ####

```
python manage.py runserver 127.0.0.1:8000

```

#### 浏览器访问 ####
```
    http://127.0.0.1:8000/
```

#### 知识点总结 ####
    testmvt项目包下目录说明：
    
    1.settings.py:包括了项目的初始化设置。可以针对整个项目有关的参数配置。例如（配置数据库，添加应用等）
    
    2.urls.py：（URLconf）这是一个URL配置表文件。主要将URL映射到应用程序上。
    
    3.wsgi.py:WSGI是Web Server Gateway Interface的缩写。WSGI是Python所选择的服务器和应用标准，Django也会使用。
              wsgi.py文件定义了我们所创建的项目都是WSGI应用。
    












































