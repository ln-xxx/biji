#### 底层实现

1. 项目中创建static文件夹（imgs/css/js）
2. 配置URL
3. 创建视图


#### 配置URL
```
from django.conf.urls import url
from django.contrib import admin
import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/.*$', views.ReadImg.as_view()),
]


```


#### 创建视图
```
#coding=utf-8
from django.http import HttpResponse, Http404, FileResponse
from django.views import View
import jsonpickle

class ReadImg(View):
    def get(self,request,*args,**kwargs):
        import re
        filepath = request.path
        m = re.match(r'^/hello/(.*)$',filepath)
        path = m.group(1)

        import os
        filedirs = os.path.join(os.getcwd(),'static/imgs',path)
        print filedirs
        if not os.path.exists(filedirs):
            raise Http404()

        response = FileResponse(open(filedirs,'rb'),content_type='image/png')
        return response

```


